#!/usr/bin/env python3
# 
# A web service to display the analysis of news articles logs.

from flask import Flask, request, redirect, url_for

from logs_analysis_db import get_most_popular_articles, get_most_popular_article_authors, get_errorenous_requests_per_day_more_than_a_percent

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Logs Analysis</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet">
    <style>
      body { font-family: "Open Sans", Helvetica, sans-serif; }
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Logs Analysis</h1>
    <div>
    <h2>What are the most popular three articles of all time?</h2>
    <ul>%s</ul>
    </div>   

    <div>
    <h2>Who are the most popular article authors of all time?</h2>
    <ul>%s</ul>
    </div>

    <div>
    <h2>On which days did more than 1%% of requests lead to errors?</h2>
    <ul>%s</ul>
    </div> 

  </body>
</html>
'''

# HTML template for an individual comment
MOST_POPULAR_ARTICLES = '''\
    <li>"%s" - %s views</li>
'''

MOST_POPULAR_ARTICLE_AUTHORS = '''\
    <li>%s - %s views</li>
'''

ERRORENOUS_REQUESTS = '''\
    <li>%s - %s%%</li>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  articles = "".join(MOST_POPULAR_ARTICLES % (title, views) for title, views in get_most_popular_articles())
  authors = "".join(MOST_POPULAR_ARTICLE_AUTHORS % (author_name, views) for author_name, views in get_most_popular_article_authors())
  errorenous_requests = "".join(ERRORENOUS_REQUESTS % (day.strftime("%b %d, %Y"), request_to_error_ratio) for day, request_to_error_ratio in get_errorenous_requests_per_day_more_than_a_percent())

  html = HTML_WRAP % (articles, authors, errorenous_requests)
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

