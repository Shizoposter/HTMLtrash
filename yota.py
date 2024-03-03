import sqlite3 as sql

database = sql.connect('file.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
sex TEXT NOT NULL,
age INTEGER)
''')

database.commit()
database.close()