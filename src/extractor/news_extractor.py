from model.article import Article
from cache.news_cache import NewsCache

from concurrent.futures import ThreadPoolExecutor

class NewsExtractor:
    
    def __init__(self, link_collector, content_extractor):
        self.link_collector = link_collector
        self.content_extractor = content_extractor
        self.cache = NewsCache()


    def extract(self, count):
        links = self.link_collector.collect(count)

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._get_article, link) for link in links]
            articles = [f.result() for f in futures]
        
        return articles


    def _get_article(self, link):
        content = self._get_content(link.url)
        return Article(link.title, link.url, content.snippet)


    def _get_content(self, url):
        content = self.cache.get_content(url)
    
        if content is None:
            content = self.content_extractor.extract(url)
            self.cache.cache_content(url, content)

        return content