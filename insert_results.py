import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bincom_test"
)
cursor = conn.cursor(dictionary=True)

# 🔹 Fetch available Polling Units
cursor.execute("SELECT uniqueid, polling_unit_name FROM polling_unit")
polling_units = cursor.fetchall()

# 🔹 Fetch available Parties
cursor.execute("SELECT DISTINCT party_abbreviation FROM announced_pu_results")
parties = cursor.fetchall()

# Display available Polling Units
print("\nAvailable Polling Units:")
for pu in polling_units:
    print(f"{pu['uniqueid']}: {pu['polling_unit_name']}")

# Get Polling Unit input
polling_unit_uniqueid = input("\nEnter Polling Unit Unique ID from the list: ")

# Display available Parties
print("\nAvailable Parties:")
for party in parties:
    print(f"- {party['party_abbreviation']}")

# Get Party input
party_abbreviation = input("\nEnter Party Abbreviation from the list: ")

# Get Score input
while True:
    try:
        party_score = int(input("\nEnter Party Score: "))
        break
    except ValueError:
        print("⚠️ Invalid input. Please enter a numeric value for the score.")

# Insert into the database
query = """
    INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score) 
    VALUES (%s, %s, %s)
"""
cursor.execute(query, (polling_unit_uniqueid, party_abbreviation, party_score))
conn.commit()

print("\n✅ New result added successfully!")

# Close connection
cursor.close()
conn.close()