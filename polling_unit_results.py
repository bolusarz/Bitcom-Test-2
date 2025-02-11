import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="ol5tz0yvwp930510.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user="dd5nl96p61stlpkk",  
    password="im8xqo3y6t3m8lni",  
    port="3306",
    database="f3lfgdazfx4amtti"
)
cursor = conn.cursor()

# Get results for a specific polling unit
polling_unit_uniqueid = input("Enter polling unit unique ID: ")

query = """
    SELECT party_abbreviation, party_score 
    FROM announced_pu_results 
    WHERE polling_unit_uniqueid = %s
"""
cursor.execute(query, (polling_unit_uniqueid,))
results = cursor.fetchall()

if results:
    print("\nResults for Polling Unit ID:", polling_unit_uniqueid)
    for party, score in results:
        print(f"{party}: {score}")
else:
    print("No results found for this polling unit.")

# Close the connection
cursor.close()
conn.close()
