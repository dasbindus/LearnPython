#! /usr/bin/env python
# Filename: SQLiteTest.py

import sqlite3

# Connect to sqlite, database name is 'test.db'
# if file not exit, then create file
conn = sqlite3.connect('test.db')
# create a cursor
cursor = conn.cursor()


# create table
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# insert data
cursor.execute('insert into user (id,name) values (\'1\', \'Baidong\')')
# get a row count
cursor.rowcount
# select SQL
cursor.execute('select * from user where id=?', '1')
# get query result
value = cursor.fetchall()
print value

# close Cursor
cursor.close()
# commit
conn.commit()
# close connection
conn.close()