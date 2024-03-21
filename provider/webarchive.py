from time import sleep
import requests
import config

class WebArchive:
    @staticmethod
    def query(url):
        while True:
            response = requests.get("https://web.archive.org/cdx/search/cdx?url={}/*&output=json&collapse=urlkey&fl=original".format(url), headers=config.headers)
            if response.status_code == 200:
                break
            sleep(1)
        result_urls = response.json()
        if result_urls:
            result_urls = result_urls[1:]
        result_urls = [item[0] for item in result_urls]
        return result_urls
