from sources.abc.abc_news import AbcNews
from sources.bbc.bbc_news import BbcNews
from sources.cnn.cnn_news import CnnNews
from sources.npr.npr_news import NprNews

from model.news_result import NewsResult

class News:

    def get_headlines(self):
        headlines = []
        headlines.append(self._get_abc())
        headlines.append(self._get_bbc())
        headlines.append(self._get_cnn())
        headlines.append(self._get_npr())

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


if __name__ == "__main__":
    headlines = News().get_headlines()

    for headline in headlines:
        print("===============================")
        print(headline.source)
        print(headline.article.title)
        print()
        print(headline.article.snippet)
        print()
        print(headline.article.url)
        print("===============================")
