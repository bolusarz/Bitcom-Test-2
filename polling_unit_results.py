import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bincom_test"
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
