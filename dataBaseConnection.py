from tkinter import *
import psycopg2
try: 
 conn = psycopg2.connect(database="flaskmovie", user="postgres", password="silverTip", host="localhost")
 print("connected")
except:
 print ("I am unable to connect to the database")
cur =conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
print(coins)
conn.commit()
cur.close()
conn.close()