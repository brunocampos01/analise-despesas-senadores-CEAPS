from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import requests
import re


def get_links_csv(url):
    """
    Function to download links csv in page
    """
    print('Try analysing page ...')
    links_pg = []

    try:
        # Testing connection
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



def dump_file_csv(links_csv, path_data):
    """
    Function to download csv
    """
    for link in links_csv:
        # last string
        file_name = link.split('/')[-1]

        # create response object 
        r = requests.get(link, stream=True)

        # download started 
        with open(path_data + 'gastos' + file_name, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
        print("\n%s downloaded!" % file_name)
