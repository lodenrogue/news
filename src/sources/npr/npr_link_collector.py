import requests
from bs4 import BeautifulSoup

from model.link import Link

BASE_URL = "https://text.npr.org"

class NprLinkCollector:

    def collect(self, count):
        main_page_resp = requests.get(BASE_URL)
        directory_soup = BeautifulSoup(main_page_resp.content, "html.parser")
        
        urls = self._get_urls(directory_soup)
        titles = self._get_titles(directory_soup)
       
        num_to_collect = min(count, len(urls))
        return [Link(urls[i], titles[i]) for i in range(0, num_to_collect)]


    def _get_titles(self, soup):
        links = soup.find_all("a", {"class" : "topic-title" })
        
        titles = []
        for link in links:
            titles.append(link.text)

        return titles


    def _get_urls(self, soup):
        links = soup.find_all("a", {"class" : "topic-title" })
        
        urls = []
        for link in links:
            urls.append("{}{}".format(BASE_URL, link["href"]))

        return urls
