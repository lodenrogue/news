from extractor.news_extractor import NewsExtractor
from sources.bbc.bbc_link_collector import BbcLinkCollector
from sources.bbc.bbc_content_extractor import BbcContentExtractor


class BbcNews():

    def get_articles(self, count):
        return (NewsExtractor(BbcLinkCollector(), BbcContentExtractor())
                .extract(count))


if __name__ == "__main__":
    articles = BbcNews().get_articles(5) 

    for article in articles:
        print("=====================================")
        print("Title:", article.title)
        print(article.snippet)
        print(article.url)
        print("=====================================")
        print()
