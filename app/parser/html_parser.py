from bs4 import BeautifulSoup


def parse(html: str):
    return BeautifulSoup(html, "lxml")