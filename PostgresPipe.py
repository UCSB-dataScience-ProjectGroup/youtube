import psycopg2 # for working with postgres
import io
import json
import pandas as pd
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
# Config.sections()  # see section csontents of config file
# Config.options('SectionOne') # see arguments in first section

Ydata = io.open(r'/Users/andiedonovan/myProjects/Youtube/Comments1.json', encoding = "utf-8")
readAll = Ydata.readlines()
#json.dumps(readAll)

#Df = pd.read_json('/Users/andiedonovan/myProjects/Youtube/Comments1.json')
#Df.to_sql(connectionstring)


conn = psycopg2.connect(Config.get('SectionOne', 'dbname', 'user', 'password')) # create a connection to databse; uses arguments provided in config.ini file
cur = conn.cursor() # Create a cursor to execute SQL commands

cur.execute("CREATE TABLE YTComments (data json);") #Create table called YTComments

#cur.executemany("INSERT INTO YTComments VALUES ('{0}')".format(readAll))
cur.execute("INSERT INTO YTComments VALUES (%s)" , readAll) # insert JSON formatted comments into table

# side notes:
# in the past two lines the cursor is executing SQL commands
# for executemanyL : second argument must always be a sequence
# ALWAYS use %s placeholder, others not supported
# source: http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries
# later, might have to look into psycopg2.sql package for dynamic entry