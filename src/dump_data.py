from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import requests
import time
import datetime
import json
import re
import os


def get_date_today():
    now = datetime.datetime.now()
    now = str(now.strftime("%Y-%m-%d"))
    return now


def drop_file(path):
    """
    Drop file each execution
    """
    try:
        if os.path.exists(path):
            os.remove(path)

    except IOError as err:
        print('IOError: ', err)
        pass


def retry(url, timeout, max_retries):
    """
    Function to retry connection in url
    """
    for retry in range(0, max_retries):
        r = requests.get(url,
                         timeout=timeout)

        if r.status_code == 200:
            return r.json()
        else:
            print('Retry: ', retry)
            time.sleep(timeout)

    raise Exception('Request Error in ', url)


def get_links_csv(url):
    """
    Function to download links csv in page
    """
    print('Try analysing page ...')
    links_pg = []

    try:
        # Testing connection
        r = requests.get(url, timeout=5)

        html = urlopen(url)

        # Create a parser instance to navigate
        page = BeautifulSoup(html, "html.parser")

        # find in tree HTML
        for link in page.find_all('a', attrs={'href': re.compile("csv")}):
            links_pg.append(link.attrs['href'])
            print(link.attrs['href'])

        return links_pg

    except HTTPError as e:
        print('HTTP error')
    except URLError as e:
        print('Server not found !')


def dump_file_json(url):
    """
    Create file data.json
    """
    clients = dump_url(url)
    today = get_date_today()

    # Prepare json
    datas = {}

    # Serialize json in data/
    data = 'data/database'+today+'.json'

    try:
        with open(data, mode='a+') as writer:  # (a+) create file if it doesn't exist and open it in append mode
            for client in clients:
                if client['enable'] == True and 'mysqlDatabaseName' in client:
                    # Create dict by store
                    store = {
                        client['id']: {
                            "host": "",
                            "user": "",
                            "password": "",
                            "database": "",
                            "charset": "UTF8"
                        }
                    }

                    # Add dict in databases
                    datas.update(store)

            json.dump(databases, writer, indent=2, ensure_ascii=False)

    except IOError as err:
        print("File Error: ", err)


def dump_file_csv(url):
    """
    Create file data.csv
    """

    today = get_date_today()
    list_links_csv = get_links_csv(url)

    # Serialize csv in data/
    data = 'data/database'+today+'.csv'

    for link in list_links_csv:
        # last string
        file_name = link.split('/')[-1]

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(data + file_name, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
        print("\n%s downloaded!" % file_name)
