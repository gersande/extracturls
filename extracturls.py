#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

url = "http://www.gersande.com/" # change this to whatever website you want to crawl through
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))
sys.stdout = open ('extractedurls.txt', 'w') # change 'extractedurls.txt' to whatever you want, and it will create a .txt file in the project (it should also work if you write a path to a file on your filesystem)

def getURL(page):
    """
    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        print(url)
    else:
        break