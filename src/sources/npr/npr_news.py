from extractor.news_extractor import NewsExtractor
from sources.npr.npr_link_collector import NprLinkCollector
from sources.npr.npr_content_extractor import NprContentExtractor


class NprNews():

    def get_articles(self, count):
        return (NewsExtractor(NprLinkCollector(), NprContentExtractor())
                .extract(count))


if __name__ == "__main__":
    articles = NprNews().get_articles(5) 

    for article in articles:
        print("=====================================")
        print("Title:", article.title)
        print(article.snippet)
        print(article.url)
        print("=====================================")
        print()
