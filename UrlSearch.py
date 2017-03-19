import sys
from crawler import Crawler
from scraper import Scraper

domain = sys.argv[1].split("//")[-1].split("/")[0]

crawler = Crawler()
crawler.crawl(sys.argv[1])

# displays the urls
print crawler.content[domain].keys()

scraper = Scraper(sys.argv[2])

for url in crawler.content[domain].keys():
    scraper.scrape(sys.argv[1]+url)