# NVD Assessment Project

## 📌 Overview
The **NVD Assessment Project** is a web application that fetches **Common Vulnerabilities and Exposures (CVE) data** from the **National Vulnerability Database (NVD) API**, stores it in a **MySQL database**, and provides an API for filtering and retrieving CVE details. A frontend UI allows users to search, sort, and view details of CVEs.

## 🚀 Features
- **Fetch CVE Data from NVD API**
- **Store Data in MySQL**
- **Retrieve CVE Data via REST API**
- **Search, Sort, and Filter CVEs**
- **View CVE Details in a Web Interface**
- **Paginated API Responses**

---

## 📥 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Praveen-Cyber311/nvd-assessment.git
cd nvd-assessment
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
```
Activate it:
```sh
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up MySQL Database**
1️⃣ Open MySQL command line and create the database:
```sql
CREATE DATABASE nvd_assessment;
USE nvd_assessment;
```
2️⃣ Create the `cve` table:
```sql
CREATE TABLE cve (
    id VARCHAR(50) PRIMARY KEY,
    description TEXT,
    score FLOAT,
    published_date DATETIME,
    last_modified DATETIME
);
```

### **5️⃣ Fetch and Store CVE Data**
```sh
python fetch_cves.py
```

---

## 🖥️ Running the Application

### **1️⃣ Start the API**
```sh
python api.py
```
API will be available at: **http://127.0.0.1:5000/cves/list**

### **2️⃣ Open the Frontend**
Open **index.html** in a web browser.

---

## 🌐 API Endpoints

### **1️⃣ Get All CVEs**
```http
GET /cves/list
```
#### **Response:**
```json
[
    {
        "id": "CVE-2023-0001",
        "description": "Security vulnerability...",
        "score": 8.5,
        "published_date": "2023-02-15T12:00:00Z",
        "last_modified": "2023-03-01T15:30:00Z"
    }
]
```

### **2️⃣ Filter CVEs**
- **By ID:** `/cves/list?cve_id=CVE-2023-0001`
- **By Year:** `/cves/list?year=2023`
- **By Score:** `/cves/list?min_score=7`
- **With Pagination:** `/cves/list?limit=10&offset=0`

---

## ✅ Running Unit Tests
```sh
pytest tests/test_api.py
```

---


![Screenshot 2025-03-01 143314](https://github.com/user-attachments/assets/17c80d4d-0467-474d-a09d-5e408ab106e0)
