from urllib.parse import urlparse
from provider.webarchive import WebArchive
from provider.commoncrawl import CommonCrawl

class Process:
    @staticmethod
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return result.scheme.lower().__eq__("http") or result.scheme.lower().__eq__("https")
        except ValueError:
            return False

    @staticmethod
    def run(url):
        if not Process.is_valid_url(url):
            print("URL seems invalid. Please check again!")
        if url.endswith("/"):
            url = url[:-1]
        result = []
        result.extend(WebArchive.query(url))
        # result.extend(CommonCrawl.query(url))
        result = list(set(result))
        print("\n".join(list(result)))
