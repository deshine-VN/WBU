from time import sleep
import requests
import config
import json

class CommonCrawl:
    @staticmethod
    def query(url):
        result_urls = []
        while True:
            response = requests.get("https://index.commoncrawl.org/CC-MAIN-2024-10-index?url={}/*&output=json&fl=url".format(url), headers=config.headers)
            if response.status_code != 503:
                break
            sleep(1)
        response = response.text.split("\n")
        if response:
            response = response[:-1]
        for item in response:
            try:
                result_urls.append(json.loads(item)["url"])
            except:
                pass
        return result_urls
