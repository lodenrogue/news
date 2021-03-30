from pathlib import Path
from model.content import Content

CACHE_DIRECTORY = "article-cache"

class NewsCache:

    def __init__(self):
        Path(CACHE_DIRECTORY).mkdir(parents=True, exist_ok=True)


    def get_content(self, url):
        file_name = self._convert_to_file_name(url)
        path = Path(f"{CACHE_DIRECTORY}/{file_name}")

        if not path.exists():
            return None

        with path.open() as f:
            snippet = f.read()

        return Content(snippet)


    def cache_content(self, url, content):
        file_name = self._convert_to_file_name(url)
        path = Path(f"{CACHE_DIRECTORY}/{file_name}")
        path.write_text(content.snippet)


    def _convert_to_file_name(self, url):
        return url.replace("/", "%2F")