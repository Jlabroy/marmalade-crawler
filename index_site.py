from crawler import Crawler
from scraper import Scraper

def index_site_func(url, userId):
    domain = url.split("//")[-1].split("/")[0]

    crawler = Crawler()
    crawler.crawl(url)

    scraper = Scraper(userId)

    for page in crawler.content[domain].keys():
        scraper.scrape(url+page)