# Liam Byrne (liambyrnenz)
# DWStats

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# Scraper created with help from https://realpython.com/python-web-scraping-practical-introduction/

URL = "http://www.chakoteya.net/DoctorWho/"


def count_occurrences(string):
    content = retrieve(URL)
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    return text.count(string)


def retrieve(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if response_ok(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        error("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def response_ok(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def error(err_string):
    print(err_string)
