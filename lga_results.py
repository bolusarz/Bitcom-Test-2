import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bincom_test"
)
cursor = conn.cursor()

# Get summed results for an LGA
lga_id = input("Enter LGA ID: ")

query = """
    SELECT apr.party_abbreviation, SUM(apr.party_score) 
    FROM announced_pu_results apr
    JOIN polling_unit pu ON apr.polling_unit_uniqueid = pu.uniqueid
    WHERE lga_id = %s
    GROUP BY apr.party_abbreviation
"""
cursor.execute(query, (lga_id,))
results = cursor.fetchall()

if results:
    print("\nTotal Results for LGA ID:", lga_id)
    for party, total_score in results:
        print(f"{party}: {total_score}")
else:
    print("No results found for this LGA.")

# Close the connection
cursor.close()
conn.close()
