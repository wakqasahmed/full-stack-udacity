# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

DBNAME = "news"

MOST_POPULAR_ARTICLES = [("Princess Shellfish Marries Prince Handsome", "1201")]
MOST_POPULAR_ARTICLE_AUTHORS = [("Ursula La Multa", "2304")]
ERRORENEOUS_REQUESTS = [("July 29, 2016", "2.5")]

def get_most_popular_articles():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from most_popular_articles")
  articles = c.fetchall()
  db.close()
  return articles
  """return reversed(POSTS)"""

def get_most_popular_article_authors():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from most_popular_article_authors")
  authors = c.fetchall()
  db.close()
  return authors
  """return reversed(POSTS)"""

def get_errorenous_requests_per_day_more_than_a_percent():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from errorenous_requests_per_day_more_than_a_percent")
  erroreneous_requests = c.fetchall()
  db.close()
  return erroreneous_requests
  """return reversed(POSTS)"""  


