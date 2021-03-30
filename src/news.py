from headline_extractor import HeadlineExtractor

class News:

    def get_headlines(self):
        return HeadlineExtractor().get_headlines()


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
