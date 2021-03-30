import requests
from bs4 import BeautifulSoup

from model.link import Link

BASE_URL = "https://lite.cnn.com"
ARTICLE_URL_TOKEN = "/article/"

class CnnLinkCollector:

    def collect(self, count):
        response = requests.get(BASE_URL)
        directory_soup = BeautifulSoup(response.content, "html.parser")
        
        urls = self._get_urls(directory_soup)
        titles = self._get_titles(directory_soup)
       
        num_to_collect = min(count, len(urls))
        return [Link(urls[i], titles[i]) for i in range(0, num_to_collect)]


    def _get_titles(self, soup):
        links = soup.find_all("a")

        titles = []
        for link in links:
            if ARTICLE_URL_TOKEN in link["href"]:
                titles.append(link.text)

        return titles
        

    def _get_urls(self, soup):
        links = soup.find_all("a")
        
        urls = []
        for link in links:
            if ARTICLE_URL_TOKEN in link["href"]:
                urls.append("{}{}".format(BASE_URL, link["href"]))
        
        return urls