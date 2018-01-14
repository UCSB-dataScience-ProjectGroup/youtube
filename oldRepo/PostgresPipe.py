import psycopg2 # for working with postgres
import io
import json
import pandas as pd
import configparser # ConfigParser in Python 2!

Config = configparser.ConfigParser() 
Config.read("config.ini")
# Config.sections()  # see section csontents of config file
# Config.options('SectionOne') # see arguments in first section

Ydata = io.open(r'~/Comments1.json', encoding = "utf-8")
readAll = Ydata.readlines()

conn = psycopg2.connect(Config.get('dbname', 'user', 'password')) # create a connection to databse; uses arguments provided in config.ini file
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
