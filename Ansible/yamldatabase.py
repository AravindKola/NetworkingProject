import yaml
import mysql.connector
# Load database configuration from YAML file
with open('yamldemo1.ymi','r') as f:
    config=yaml.safe_load(f)['database']
# Connect to database
conn=mysql.connector.connect(
    host=config['host'],
    port=config['port'],
    database=config['dbname'],
    user=config['user'],
    password=config['password']
)
# Do something with the database connection
cur=conn.cursor()
cur.execute("SELECT * FROM customer")
rows=cur.fetchall()
for row in rows:
    print(row)
# Close the database connection when finished
cur.close()
conn.close()

