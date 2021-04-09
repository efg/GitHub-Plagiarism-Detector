import re

import requests
from bs4 import BeautifulSoup


def extract_info(text: str) -> tuple:
    """return team name and code similarty """
    if not text:
        raise ValueError('Empty link name')
    print(text)
    text_split = re.split(r'/', text)
    if len(text_split) < 2:
        raise ValueError('Inefficient link length')
    tname = re.split('_', text_split[-2])[1]
    similarity = re.split(r"[(%)]", text_split[-1])[1]
    return (tname, float(similarity))


def scrape_MOSS_report(URL: str) -> list:
    """
        parse given string to extract team name and corresponding 
        similarity score 
    """

    page = requests.get(URL)
    if page.status_code >= 400:
        raise ValueError(f'{URL} does not exists')

    soup = BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find_all('table')  # contains all similarities

    list_tname_similarity = []

    for row in table_rows:
        links = row.find_all('a')
        n = len(links)
        for i in range(0, n, 2):  # pick couple of links
            first, second = links[i], links[i + 1]
            # [(('t1', 69), ('t2', 22))]
            list_tname_similarity += [(extract_info(first.getText()),
                                       extract_info(second.getText()))]

    return list_tname_similarity
