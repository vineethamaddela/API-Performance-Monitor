import requests
import time
import csv
import sqlite3
import schedule

def check_api():
    url = "https://jsonplaceholder.typicode.com/posts"

    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    response_time = end_time - start_time

    print("API URL:", url)
    print("Status Code:", response.status_code)
    print("Response Time:", round(response_time, 3), "seconds")

    with open("api_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["API URL", "Status Code", "Response Time (seconds)"])
        writer.writerow([url, response.status_code, round(response_time, 3)])

    print("Data saved to api_report.csv")

    conn = sqlite3.connect("api_monitor.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_url TEXT,
        status_code INTEGER,
        response_time REAL
    )
    """)

    cursor.execute(
        "INSERT INTO api_logs (api_url, status_code, response_time) VALUES (?, ?, ?)",
        (url, response.status_code, round(response_time, 3))
    )

    conn.commit()
    conn.close()

    print("Data saved to api_monitor.db")


schedule.every(10).seconds.do(check_api)

check_api()

while True:
    schedule.run_pending()
    time.sleep(1)
