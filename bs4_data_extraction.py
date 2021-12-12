import html2text
from bs4 import BeautifulSoup
import re
import json
import unicodedata


try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    # getting response object for the request
    souper = ""
    def getdocument(weburl):
        souper = ""
        try:
            page = requests.get(weburl, headers=headers, timeout=40)
            souper = BeautifulSoup(page.text, 'html.parser')
            str_unwanted = souper.find_all('script')
            for tag in str_unwanted:
                tag.decompose()
            return souper
        except Exception as exe:
            pass
            # print('Exception error occured in getDocument().scraping---%s', exe)
except Exception as ex:
    print('Exception error occured in scraping (Main method)', ex)


def main_pipeline(url):
    try:
        html_content = getdocument(url)
        hand = html2text.HTML2Text()
        # body = html_content.find("div",{"id":"body"}).text
        body = html_content.find("body").text
        print("body:", body)
        body_tag = hand.handle(body)
    except Exception as ex:
        print('Exception error occured in main_pipeline', ex)
    # return body, body_tag


# if __name__ == "__main__":
    # url = "https://www.grandviewresearch.com/industry-analysis/tpu-films-industry"
    url = "https://www.marketsandmarkets.com/Market-Reports/industrial-sensor-market-108042398.html"
    print(main_pipeline(url))

