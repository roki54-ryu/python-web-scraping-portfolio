# 🚀 Python Web Scraping & API Portfolio

A collection of practical Python scripts for extracting data from websites and APIs, processing it with Pandas, and saving it to Excel.

---

## 📂 Projects Included

### 1. MediaMarkt Product Scraper (`mediamarkt_scraper.py`)
* **Description:** Extracts product names and prices from MediaMarkt category pages using `BeautifulSoup`.
* **Tech Stack:** Python, Requests, BeautifulSoup, Pandas.
* **Output:** Saves clean data into an `.xlsx` file (`iphone_prices.xlsx`).
* **Key Features:** Handles missing HTML elements gracefully to prevent script crashes.

### 2. Remote Jobs API Aggregator (`remote_jobs_aggregator.py`)
* **Description:** Fetches remote job listings programmatically via JSON API endpoints with built-in pagination handling (`while` loops and cursors).
* **Tech Stack:** Python, Requests, Pandas.
* **Output:** Exports structured job data into an Excel spreadsheet.
* **Key Features:** Efficient data extraction using API parameters instead of heavy HTML parsing.

---

## 🛠️ Requirements & Installation
To run these scripts, make sure you have Python installed, then install the required libraries:

```bash
pip install requests beautifulsoup4 pandas openpyxl
