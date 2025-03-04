from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="praveen",  # Replace with your MySQL password
        database="nvd_assessment"
    )

# API to fetch CVE data
@app.route("/cves/list", methods=["GET"])
def get_cves():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM cve WHERE 1=1"
    params = []

    if request.args.get("cve_id"):
        query += " AND id = %s"
        params.append(request.args.get("cve_id"))

    if request.args.get("year"):
        query += " AND YEAR(published_date) = %s"
        params.append(request.args.get("year"))

    if request.args.get("min_score"):
        query += " AND score >= %s"
        params.append(float(request.args.get("min_score")))

    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
