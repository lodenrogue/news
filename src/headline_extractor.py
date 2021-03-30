from sources.abc.abc_news import AbcNews
from sources.bbc.bbc_news import BbcNews
from sources.cnn.cnn_news import CnnNews
from sources.npr.npr_news import NprNews

from model.news_result import NewsResult

from concurrent.futures import ThreadPoolExecutor


class HeadlineExtractor:

    def get_headlines(self):
        get_calls = ([
            self._get_abc,
            self._get_bbc,
            self._get_cnn,
            self._get_npr])

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(call) for call in get_calls]
            headlines = [f.result() for f in futures]
        
        return headlines


    def _get_npr(self):
        return self._get("NPR", NprNews())


    def _get_cnn(self):
        return self._get("CNN", CnnNews())


    def _get_bbc(self):
        return self._get("BBC News", BbcNews())


    def _get_abc(self):
        return self._get("ABC News", AbcNews())


    def _get(self, name, source):
        article = source.get_articles(1)[0]
        return NewsResult(name, article)
