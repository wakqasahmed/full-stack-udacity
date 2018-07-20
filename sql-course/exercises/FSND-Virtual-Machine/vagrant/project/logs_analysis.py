#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

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
    <ul>
      <li>"Princess Shellfish Marries Prince Handsome" - 1201 views</li>
      <li>"Baltimore Ravens Defeat Rhode Island Shoggoths" - 915 views</li>
      <li>"Political Scandal Ends In Political Scandal" - 553 views</li>
    </ul>
    </div>

    <div>
    <h2>Who are the most popular article authors of all time?</h2>
    <ul>
      <li>Ursula La Multa - 2304 views</li>
      <li>Rudolf von Treppenwitz - 1985 views</li>
      <li>Markoff Chaney - 1723 views</li>
      <li>Anonymous Contributor - 1023 views</li>
    </ul>
    </div>

    <div>
    <h2>On which days did more than 1% of requests lead to errors?</h2>
    <ul>
      <li>July 29, 2016 - 2.5% errors</li>
    </ul>
    </div>    

    <!-- post content will go here -->

  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=title>%s</em> - %s views</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  articles = "".join(POST % (title, views) for title, views in get_most_popular_articles())
  html = HTML_WRAP# % articles
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

