import psycopg2
import urllib
import os
from bs4 import BeautifulSoup
from goose import Goose

class Scraper(object):
    def __init__(self, user_id):
        self.db = psycopg2.connect(database=os.environ['DATABASE_NAME'],
                                   user=os.environ['DATABASE_USER'],
                                   password=os.environ['DATABASE_PASSWORD'],
                                   host=os.environ['DATABASE_HOST'],
                                   port=os.environ['DATABASE_PORT'],
                                   sslmode='require')

        self.cur = self.db.cursor()
        self.user_id = user_id

    def scrape(self, url):
        g = Goose()
        article = g.extract(url=url)

        print(article.title);

        ######
        query = 'INSERT INTO pages (user_id, url, title, meta_description, content) VALUES (%s, %s, %s, %s, %s)'
        self.cur.execute(query, (self.user_id, url, article.title, article.meta_description, article.cleaned_text))
        self.db.commit()

        #####

        print('inserted %s into db' % url)
