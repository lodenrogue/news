from sources.abc.abc_news import AbcNews
from sources.bbc.bbc_news import BbcNews
from sources.cnn.cnn_news import CnnNews
from sources.npr.npr_news import NprNews


SOURCE_MAP = {
    "abc": AbcNews(),
    "bbc": BbcNews(),
    "cnn": CnnNews(),
    "npr": NprNews()
}


class SourceExtractor:

    def get_from_source(self, source, count):
        source_lowercase = source.lower()

        if source_lowercase not in SOURCE_MAP:
            return []

        return SOURCE_MAP[source_lowercase].get_articles(count)