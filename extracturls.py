#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = "http://www.gersande.com"
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))


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
