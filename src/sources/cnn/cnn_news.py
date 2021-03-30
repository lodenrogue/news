from extractor.news_extractor import NewsExtractor
from sources.cnn.cnn_link_collector import CnnLinkCollector
from sources.cnn.cnn_content_extractor import CnnContentExtractor


class CnnNews():

    def get_articles(self, count):
        return (NewsExtractor(CnnLinkCollector(), CnnContentExtractor())
                .extract(count))


if __name__ == "__main__":
    articles = CnnNews().get_articles(5) 

    for article in articles:
        print("=====================================")
        print("Title:", article.title)
        print(article.snippet)
        print(article.url)
        print("=====================================")
        print()
