import psycopg2
import time

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname="promosfusion-iam", 
    user="service", 
    password="password", 
    host="localhost", 
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query

last_time = time.time()
cur.execute("SELECT * FROM public.user WHERE id = 1 ORDER BY id ASC")
records = cur.fetchall()
print("Extract [db]: ", time.time() - last_time)

# Close communication with the database
cur.close()
conn.close()

# Print results
for record in records:
    print(record)
