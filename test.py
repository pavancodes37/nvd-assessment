import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this if you're using a different user
    password="praveen",  # Replace with your MySQL root password
    database="nvd_assessment"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")

print("Connected to MySQL successfully! Available tables:")
for table in cursor:
    print(table)

conn.close()
