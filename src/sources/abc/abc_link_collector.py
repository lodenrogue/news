import requests
from bs4 import BeautifulSoup

from model.link import Link

BASE_URL = "https://abcnews.go.com/"

class AbcLinkCollector:

    def collect(self, count):
        response = requests.get(BASE_URL)
        directory_soup = BeautifulSoup(response.content, "html.parser")
        
        urls = self._get_urls(directory_soup)
        titles = self._get_titles(directory_soup)
       
        num_to_collect = min(count, len(urls))
        return [Link(urls[i], titles[i]) for i in range(0, num_to_collect)]


    def _get_titles(self, soup):
        return self._get_data(soup, lambda link: link.text)


    def _get_urls(self, soup):
        return self._get_data(soup, lambda link : link["href"])


    def _get_data(self, soup, strategy):
        section = soup.find(id="trio-headline-view")
        unordered_list = section.find("ul")
        items = unordered_list.find_all("li")

        data = []
        for item in items:
            div = item.find("div", {"class": "headlines-li-div"})
            header = div.find("h1")
            link = header.find("a")
            data.append(strategy(link))

        return data
