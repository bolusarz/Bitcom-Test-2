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
