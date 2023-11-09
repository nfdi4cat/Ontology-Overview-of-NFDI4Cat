# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:03:30 2023

@author: smaxbehr
"""

import requests
from bs4 import BeautifulSoup

ontoList = ["BFO", "BAO"]
# Send an HTTP GET request to the webpage
for i in [1,2]:
    response = requests.get("https://bioportal.bioontology.org/mappings/AFO?page={}&target=https%3A%2F%2Fdata.bioontology.org%2Fontologies%2F{}".format(str(i),ontoList[0]))
# "h""
# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table class')#, class_='zebra')

# Find the title element and extract its text
title = soup.title.text

# Print the title
print(title)