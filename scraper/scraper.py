# Liam Byrne (liambyrnenz)
# DWStats

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from scraper import pageinfo

# Scraper created with help from https://realpython.com/python-web-scraping-practical-introduction/

URL = "http://www.chakoteya.net/DoctorWho/"

# ================================ HTTP ACCESS ================================


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

# ================================== SCRAPER ==================================


def run_scraper():
    """
    Run the scraper for all episodes as defined in the pageinfo module.
    """
    for (season, episode_count) in pageinfo.SEASONS_AND_EPISODES:
        for episode in range(episode_count):
            content = retrieve(URL + season + "-" + episode + pageinfo.extension(season))
            soup = BeautifulSoup(content, "html.parser")


def count_occurrences(string, url):
    """
    Count and return the number of occurrences of a given string in a web page defined by the given URL.
    :param string: string to search for in page
    :param url: URL of web page
    :return: number of occurrences of string in web page hosted at URL
    """
    content = retrieve(url)
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    return text.count(string)
