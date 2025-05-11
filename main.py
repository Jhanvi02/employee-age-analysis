import sqlite3
import requests
from database import setup_database

# --- Step 1: Setup DB
setup_database()

# --- Step 2: Register webhook
response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json={
        "name": "John Doe",
        "regNo": "REG12347",
        "email": "john@example.com"
    }
)

data = response.json()
webhook_url = data["webhook"]
access_token = data["accessToken"]

# --- Step 3: Solve the SQL Problem
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

query = '''
SELECT 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE e1
JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN EMPLOYEE e2 
    ON e1.DEPARTMENT = e2.DEPARTMENT 
    AND DATE(e2.DOB) > DATE(e1.DOB)
GROUP BY e1.EMP_ID
ORDER BY e1.EMP_ID DESC;
'''

cursor.execute(query)
result = cursor.fetchall()
conn.close()

# Save the final query to file (for GitHub reference)
with open("query.sql", "w") as f:
    f.write(query.strip())

# --- Step 4: Send final query back
submit_response = requests.post(
    webhook_url,
    headers={
        "Authorization": access_token,
        "Content-Type": "application/json"
    },
    json={"finalQuery": query.strip()}
)

print("Submission response:", submit_response.status_code, submit_response.text)