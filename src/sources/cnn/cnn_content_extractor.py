from newspaper import Article
from model.content import Content

SNIPPET_LENGTH = 200
SOURCE_PREFIX = "Source: CNN"
EDITOR_PREFIX = "Editor's Note:"

class CnnContentExtractor:

    def extract(self, url):
        snippet = self._get_snippet(url)
        return Content(snippet)


    def _get_snippet(self, url):
        article = Article(url)
        article.download()
        article.parse()
        
        text = article.text
        if text is None:
            return ""
        
        cleaned = self._clean_text(text)
        if len(cleaned) < SNIPPET_LENGTH:
            return cleaned
       
        return cleaned[0 : SNIPPET_LENGTH].rstrip() + "..."


    def _clean_text(self, text):
        result = ""
        
        for line in text.split("\n"):
            if self._is_article_line(line) and len(line) > 0:
                result += line + " "
       
        return result        


    def _is_article_line(self, line):
        return (line.startswith(SOURCE_PREFIX) == False 
            and line.startswith(EDITOR_PREFIX) == False)