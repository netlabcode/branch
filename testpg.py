import psycopg2
 
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")
 
if conn is not None:
    print('Connection established to PostgreSQL.')
else:
    print('Connection not established to PostgreSQL.')