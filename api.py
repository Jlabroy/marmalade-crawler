from flask import Flask
from flask import request
import json
from crawler import Crawler
from scraper import Scraper

app = Flask(__name__)

@app.route("/")
def main():
    try:
        url = request.args.get('url')
        userId = request.args.get('userId')

        domain = url.split("//")[-1].split("/")[0]

        crawler = Crawler()
        crawler.crawl(url)

        scraper = Scraper(userId)

        for url in crawler.content[domain].keys():
            scraper.scrape(domain+url)

        return json.dumps(True)
    except:
        return json.dumps(False)

if __name__ == "__main__":
    app.run()