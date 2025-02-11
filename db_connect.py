import mysql.connector

# Connect to MySQL

conn = mysql.connector.connect(
    host="ol5tz0yvwp930510.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user="dd5nl96p61stlpkk",  
    password="im8xqo3y6t3m8lni",  
    port="3306",
    database="f3lfgdazfx4amtti"
)

if conn.is_connected():
    print("✅ Successfully connected to MySQL!")

conn.close()
