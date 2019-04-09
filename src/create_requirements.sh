#!/bin/bash
# Description:   Create file with requirements
# Author:        brunocampos01
# Input:         N/A
# Output:  requirements.txt
# ----------------------------------- #

# Convert files .ipynb to python
jupyter nbconvert --to python notebooks/*.ipynb

# Generate requirements
pipreqs notebooks/ --force

# Remove converted files
rm -rf notebooks/*.py

echo -e "\n\bRequirements this project:\n"
cat notebooks/requirements.txt

# Mv file
mv notebooks/requirements.txt .
