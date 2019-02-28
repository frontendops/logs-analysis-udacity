""" main file for all functionality"""
import psycopg2

dbName = "news"
# all of the questions for the project
question1 = "What are the most popular three articles of all time? \n"
question2 = "Who are the most popular article authors of all time? \n"
question3 = "On which days did more than 1 % of requests lead to errors? \n"

# queries that get passed into db function
query1 = "select title,count(title) as views from articles join log on log.path = concat('/article/',articles.slug) group by title order by views desc limit 3"

query2 = "select name, count(name) as views from articles join authors on articles.author = authors.id join log on log.path = concat('/article/',articles.slug) group by authors.name order by views desc limit 4;"

query3 = "select * from articles"


# connecting to the db and getting the result of the query passed in
def connectDB(query):
    db = psycopg2.connect(database=dbName)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

# this connects to the db and prints the result
# print(connectDB())


print(question1)
print(connectDB(query1))
print("\n")

print(question2)
print(connectDB(query2))
print("\n")

# print(question3)

# full query 2
"""
    select name, count(name) as views 
        from articles
            join authors
            on articles.author = authors.id
                join log
                on log.path = concat('/article/',articles.slug)
            group by authors.name
                order by views desc limit 4;
"""
