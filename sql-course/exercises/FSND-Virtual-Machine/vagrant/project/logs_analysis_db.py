# "Database code" for the DB News.

import datetime
import psycopg2
import bleach

def get_most_popular_articles(conn):
    """Return three most accessed articles of all time,
    sorted list with the most popular article at the top."""
    c = conn.cursor()
    c.execute("select * from most_popular_articles")
    articles = c.fetchall()
    return articles


def get_most_popular_article_authors(conn):
    """Return authors who got the most page views,
    sorted list with the most popular author at the top."""
    c = conn.cursor()
    c.execute("select * from most_popular_article_authors")
    authors = c.fetchall()
    return authors


def get_erroneous_requests_per_day_gt_a_percent(conn):
    """Return day and error rate in percent for the days when
    more than 1% of requests lead to errors."""
    c = conn.cursor()
    c.execute("select * from erroneous_requests_per_day_more_than_a_percent")
    erroneous_requests = c.fetchall()
    return erroneous_requests

DBNAME = "news"
conn = psycopg2.connect("dbname=" + DBNAME)
most_popular_articles = get_most_popular_articles(conn)
most_popular_article_authors = get_most_popular_article_authors(conn)
erroneous_requests_per_day_gt_a_percent = get_erroneous_requests_per_day_gt_a_percent(conn)
conn.close()
