from flask import Flask
from flask import request
import json
import os
from crawler import Crawler
from scraper import Scraper
from rq import Queue
from worker import conn
from index_site import index_site

app = Flask(__name__)
q = Queue(connection=conn)

@app.route("/")
def main():
    url = request.args.get('url')
    userId = request.args.get('userId')

    q.enqueue(index_site, url, userId)
    return json.dumps(True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)