from urllib.parse import urlparse
from provider.webarchive import WebArchive
from provider.commoncrawl import CommonCrawl
import os

class Process:
    @staticmethod
    def sitemap(url, waybackurls):
        result = {}
        result[url] = ""
        for waybackurl in waybackurls:
            paths = waybackurl.replace(url, "").split("/")
            while paths:
                result[url + "/".join(paths)] = ""
                paths = paths[:-1]
        return list(result.keys())
        with open(os.getcwd() + "/test.txt", "w") as file:
            file.write("\n".join(list(result.keys())))
        # print("\n".join(list(result.keys())))

    @staticmethod
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return result.scheme.lower().__eq__("http") or result.scheme.lower().__eq__("https")
        except ValueError:
            return False

    @staticmethod
    def run(url, is_sitemap, output):
        if not Process.is_valid_url(url):
            print("URL seems invalid. Please check again!")
        if url.endswith("/"):
            url = url[:-1]
        result = []
        result.extend(WebArchive.query(url))
        result.extend(CommonCrawl.query(url))
        result = list(set(result))
        result = result
        print(len(result))

        if is_sitemap:
            result = Process.sitemap(url, result)
        
        with open(output, "w") as file:
            file.write("\n".join(result))