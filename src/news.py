import argparse

from headline_extractor import HeadlineExtractor
from source_extractor import SourceExtractor

class News:

    def get_headlines(self):
        return HeadlineExtractor().get_headlines()


    def get_from_source(self, source, count):
        return SourceExtractor().get_from_source(source, count)

##########################################################

def get_args():
    parser = argparse.ArgumentParser()
    
    (parser.add_argument(
        "-s", 
        "--source", 
        help="source target for news extraction"))

    (parser.add_argument(
        "-c", 
        "--count", 
        type=int, 
        help="maximun number of results to return when extracting by source"))

    return parser.parse_args()


def print_article(article):
    print(article.title)
    print()
    print(article.snippet)
    print()
    print(article.url)


if __name__ == "__main__":
    args = get_args()
    count = args.count if args.count is not None else 5

    if args.source is not None:
        articles = News().get_from_source(args.source, count)

        for article in articles:
           print("===============================")
           print_article(article)
           print("===============================")

    else:
        headlines = News().get_headlines()

        for headline in headlines:
            print("===============================")
            print(headline.source)
            print_article(headline.article)
            print("===============================")

