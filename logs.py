#! /usr/bin/env python3

""" main file for all functionality"""
import psycopg2

dbName = "news"
# all of the questions for the project
question1 = "What are the most popular three articles of all time?:"
question2 = "Who are the most popular article authors of all time?"
question3 = "On which days did more than 1 % of requests lead to errors?"

# queries that get passed into db function
query1 = "select title,count(title) as impressions " \
    "from articles join log on log.path = concat('/article/',articles.slug) " \
    "group by title order by impressions desc limit 3"

query2 = "select name, count(name) as impressions " \
    "from articles join authors on articles.author = authors.id " \
    "join log on log.path = concat('/article/',articles.slug) " \
    "group by authors.name order by impressions desc limit 4;"

query3 = "select dates.day, round(100.0*totalErrors/days,2) as percent " \
    "from dates, errorDate where dates.day = errorDate.day " \
    "group by dates.day, percent order by percent desc limit 1;"


# connecting to the db and getting the result of the query passed in
# added error handling
def connectDB(query):
    if __name__ == "__main__":
        try:
            db = psycopg2.connect(database=dbName)
            cursor = db.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            db.close()
            return results
        except psycopg2.Error as error:
            print(error)


# this connects to the db and prints the result
# formatResponse is a pure function that takes args to display output
# the type argument is for either the word views or a % sign


def formatResponse(question, query, type):
    print(question)
    for (title, count) in connectDB(query):
        print("    {} - {} {}" .format(title, count, type))

    print('-' * 50)


# calling each response
formatResponse(question1, query1, "views")

formatResponse(question2, query2, "views")

formatResponse(question3, query3, "%")


# full queries and views for easier viewing
# full query 2
"""
    select name, count(name) as views from articles
            join authors
            on articles.author = authors.id
                join log
                on log.path = concat('/article/',articles.slug)
            group by authors.name
                order by views desc limit 4;
"""

# full query 3
# convert total errors into percent
"""
select dates.day, round(100.0*totalErrors/days,2) as percent
    from dates, errorDate
       where dates.day = errorDate.day
        group by dates.day, percent
        order by percent desc limit 1;
"""
