#!/usr/bin/env python3

# using Postgresql
import psycopg2


# query_1 stores most popular three articles of all time
query_1 = """select articles.title, count(*) as num from logs, articles where
log.status='200 OK' and articles.slug = subdtr(log.path,10) group by
articles.title order by num desc limit 3;"""

# query_2 stores most popular article authors of all time
query_2 = """select article.authors, count(*) as num from logs, articles where
log.status='200 OK' and articles.slug = subdtr(log.path,10) group by
articles.name order by num desc;"""

# query_3 stores on which day more than 1% of requests lead to errors
query_3 = """select time, percentagefailed from percentagecount where
percentagefailed > 1;"""

# establishing a connection and fetching data by executing the query send in
argument


def db_query(query):
    db = psycopg2.connect(database="name")
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    return data

# prints the top three articles of all time


def top_3_articles():
    top_3_articles = db_query(query_1)
    print("\n1.Most popular 3 articles of all time\n")
    for title, num in top_3_articles:
        print("  \"{}\" --> {} views".format(title, num))

# prints most popular article authors of all time


def top_authors():
    top_authors = db_query(query_2)
    print("\n2.Top authors of all time\n")
    for name, num in top_authors:
        print("  {} --> {} views".format(name, num))

# prints days on which more than 1% of the requests lead to error


def max_error():
    high_error_days = db_query(query_3)
    print("\n3.Days with more than 1% of requets leading to error\n")
    for day, percentagefailed in high_error_days:
        print(
            """  {0:%B %d, %Y} --> {1:.1f} % errors""",
            format(day, percentagefailed)
        )

if __name__ == '__main__':
    print("\nOutput of logs_analysis.py\n")
    top_3_articles()
    top_authors()
    max_error()

