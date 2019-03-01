# Logs Analysis Project 
## Python and SQL

## About

Project for Udacity Full stack Nanodegree, using python and SQL to retrieve information from a large newspaper database. 3 main tables `articles`, `authors`, `log`. 

## What I learned

- SQL queries
  - Joining tables
  - Creating Views
  - Grouping and Ordering

- Connecting python with a database

- Running a Linux Virtual Machine on Mac os

## Views needed to run correctly

 In order to the the expected results. You must create these views when running psql.

 ### view 1

 ```
    CREATE VIEW dates AS
        SELECT  to_char(time, 'DD-MM-YYYY') as day,
        count(*) as days
        FROM log
        GROUP BY day;
 ```

 ### view 2
 ```
    CREATE VIEW errorDate AS
        SELECT to_char(time, 'DD-MM-YYYY') as day, count(*) as totalErrors
        FROM log
        WHERE status = '404 NOT FOUND'
        GROUP BY day;
 ```


## To get started

1. Download a VM udacity recomends `Udacity vm here`

2. Download the Db here `db here` and drag db into vagrant folder

3. Use `vagrant up` and `vagrant ssh` 

4. Dowload the [database][https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip] and Copy it in the `vagrant` folder

5. Load the Data with `psql -d news -f newsdata.sql`

6. Conally connect to the db with `psql -d news`

Using python with the `psycopg2` module we connect to our SQL database.

