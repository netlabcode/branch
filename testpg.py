import psycopg2
 
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")

#Check Connection
"""
if conn is not None:
    print('Connection established to PostgreSQL.')
else:
    print('Connection not established to PostgreSQL.')
"""

#Setting auto commit 
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO test(val, dec) VALUES (33, -123.123456)''')

cursor.close()
conn.close()