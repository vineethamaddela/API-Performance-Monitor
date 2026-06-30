# API Performance Monitor

## Description
This project monitors the performance of an API by checking its response status and response time at regular intervals.

## Features
- Checks API status code
- Measures response time
- Saves data to CSV file
- Saves data to SQLite database
- Runs automatically every 10 seconds using the schedule library

## Technologies Used
- Python
- Requests
- CSV
- SQLite3
- Schedule

## Files
- api_monitor.py - Main Python program
- api_report.csv - Stores API monitoring data
- api_monitor.db - SQLite database
- README.md - Project documentation

## How to Run
1. Install the required libraries:
   pip install requests schedule

2. Run the program:
   python api_monitor.py

## Output
The program displays:
- API URL
- Status Code
- Response Time

It also saves the data into:
- api_report.csv
- api_monitor.db
