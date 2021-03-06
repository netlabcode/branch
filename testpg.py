import psycopg2
from datetime import datetime
 
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

dt = datetime.now()

inserted_values = (
        dt,
        123456.123456789123456,
        123
    )

# INSTER VALUE TO TABLE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
cursor.execute(" INSERT INTO test(dtime, dec, val) VALUES (%s,%s,%s)", inserted_values)

"""
# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO test(val, dec, dtime) VALUES (33, -999.123456, dt)''')
"""


cursor.close()
conn.close()