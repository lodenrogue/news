import unittest
from news import News

class NewsTest(unittest.TestCase):

    def test_get_from_abc_source(self):
        self._test_get_from_source("abc", 3)


    def test_get_from_bbc_source(self):
        self._test_get_from_source("bbc", 3)


    def test_get_from_cnn_source(self):
        self._test_get_from_source("cnn", 3)


    def test_get_from_npr_source(self):
        self._test_get_from_source("npr", 3)


    def _test_get_from_source(self, source, count):
        articles = News().get_from_source(source, count)
        self.assertEqual(count, len(articles), "Result length is correct")

        for article in articles:
            self.assertIsNotNone(article.url, "Article url is not None")
            self.assertIsNotNone(article.title, "Article title is not None")
            self.assertIsNotNone(article.snippet, "Article snippet is not None")


if __name__ == '__main__':
    unittest.main()
