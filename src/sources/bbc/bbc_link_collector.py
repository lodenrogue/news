import requests
from bs4 import BeautifulSoup

from model.link import Link

INDEX_URL = "https://readspike.com/"

class BbcLinkCollector:

    def collect(self, count):
        response = requests.get(INDEX_URL)
        directory_soup = BeautifulSoup(response.content, "html.parser")
        
        urls = self._get_urls(directory_soup)
        titles = self._get_titles(directory_soup)
        
        num_to_collect = min(count, len(urls))
        return [Link(urls[i], titles[i]) for i in range(0, num_to_collect)]


    def _get_titles(self, soup):
        ordered_list = soup.find("ol", {"class": "links-list--bbc"})
        items = ordered_list.find_all("li")

        titles = []
        for item in items:
            link = item.find("a")
            titles.append(link.text)
        
        return titles


    def _get_urls(self, soup):
        ordered_list = soup.find("ol", {"class": "links-list--bbc"})
        items = ordered_list.find_all("li")

        urls = []
        for item in items:
            link = item.find("a")
            urls.append(link["href"])
        
        return urls