import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP username
    password="",  # Default XAMPP password (empty)
    database="bincom_test"
)

if conn.is_connected():
    print("✅ Successfully connected to MySQL!")

conn.close()
