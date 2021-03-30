from extractor.news_extractor import NewsExtractor
from sources.abc.abc_link_collector import AbcLinkCollector
from sources.abc.abc_content_extractor import AbcContentExtractor


class AbcNews():

    def get_articles(self, count):
        return (NewsExtractor(AbcLinkCollector(), AbcContentExtractor())
                .extract(count))


if __name__ == "__main__":
    articles = AbcNews().get_articles(5) 

    for article in articles:
        print("=====================================")
        print("Title:", article.title)
        print(article.snippet)
        print(article.url)
        print("=====================================")
        print()
