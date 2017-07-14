#!/usr/bin/env python2.7

import psycopg2
DB = "news"

# query to select the most popular three articles of all time
query_title = (
    "select articles.title, count(*) "
    "from articles, log "
    "where log.path like concat ('%', articles.slug) "
    "and log.status = '200 OK'"
    "group by articles.title "
    "order by count desc limit 3;"
)

# query to select the most popular article authors of all time
query_author = (
    "select authors.name, count(*) "
    "from authors, articles, log "
    "where log.path like concat ('%', articles.slug) "
    "and log.status = '200 OK' "
    "and authors.id = articles.author "
    "group by authors.name "
    "order by count desc;"
)

# query to select which days did more than 1% of requests lead to errors
query_error = (
    "select day, percentage from ("
    "select day, round((sum(numerator)/(select count(*) from log where "
    "date(time) = day) * 100), 2) as percentage from "
    "(select date(time) as day, count (*) as numerator from log "
    "where status not like '%200%' group by day) "
    "as log_percentage group by day order by percentage desc) as final_query "
    "where percentage >= 1"
)


def call_query_title():
    c = db.cursor()
    try:
        c.execute(query_title)
    except:
        print "I am unable to select from DB for query_article"
    rows = c.fetchall()
    print "\n    Three most popular articles of all time:   \n"
    for row in rows:
        print "   ", row[0], " -- ", row[1], " (views)"
    return


def call_query_author():
    c = db.cursor()
    try:
        c.execute(query_author)
    except:
        print "I am unable to select from DB for query_author"
    rows = c.fetchall()
    print "\n    The most popular author of all time:   \n"
    for row in rows:
        print "   ", row[0], " -- ", row[1], " (views)"
    return


def call_query_error():
    c = db.cursor()
    try:
        c.execute(query_error)
    except:
        print "I am unable to select from DB for query_error"
    rows = c.fetchall()
    print "\n    Error Rate:   \n"
    for row in rows:
        print "   ", row[0], "--", row[1], '% errors'
    return


# Connect to "news" database
try:
    db = psycopg2.connect(database=DB)
except:
    print "I am unable to connect to the database"


call_query_title()
call_query_author()
call_query_error()
db.close()
