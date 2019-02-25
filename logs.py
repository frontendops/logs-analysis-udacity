""" main file for all functionality"""
import psycopg2

dbName = "news"
# all of the questions for the project
question1 = "What are the most popular three articles of all time? \n"
question2 = "Who are the most popular article authors of all time? \n"
question3 = "On which days did more than 1 % of requests lead to errors? \n"

# queries that get passed into db function
query1 = "select title from articles  join authors on articles.author = authors.id"
query2 = "select * from authors"
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

# print(question2)
# print(question3)
