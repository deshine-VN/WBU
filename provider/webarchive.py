import requests
import config

class WebArchive:
    @staticmethod
    def query(url):
        result_urls = requests.get("https://web.archive.org/cdx/search/cdx?url={}/*&output=json&collapse=urlkey&fl=original".format(url), headers=config.headers).json()
        if result_urls:
            result_urls = result_urls[1:]
        result_urls = [item[0] for item in result_urls]
        return result_urls