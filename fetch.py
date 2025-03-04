import requests
import mysql.connector

# NVD API URL
API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Function to fetch CVE data from API
def fetch_cve_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # Replace with your MySQL username
        password="praveen",  # Replace with your MySQL password
        database="nvd_assessment"
    )

# Store CVE data in MySQL
def store_data(cve_list):
    conn = connect_db()
    cursor = conn.cursor()

    for item in cve_list:
        cve = item["cve"]  # Access the 'cve' dictionary

        cve_id = cve["id"]  # Check if 'id' exists inside 'cve'
        description = cve["descriptions"][0]["value"] if "descriptions" in cve else "No description"
        score = cve.get("metrics", {}).get("cvssMetricV3", [{}])[0].get("cvssData", {}).get("baseScore", None)
        published = cve.get("published", "0000-00-00T00:00:00Z")
        modified = cve.get("lastModified", "0000-00-00T00:00:00Z")

        cursor.execute("""
            INSERT INTO cve (id, description, score, published_date, last_modified) 
            VALUES (%s, %s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
            description=VALUES(description), score=VALUES(score), published_date=VALUES(published_date), last_modified=VALUES(last_modified)
        """, (cve_id, description, score, published, modified))

    conn.commit()
    conn.close()


# Fetch and store data
data = fetch_cve_data()
if data:
    store_data(data["vulnerabilities"])
