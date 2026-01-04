# Weather Data API (Flask) 🌦️

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20API-success)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A Flask-based Weather Data API that provides historical temperature data for weather stations using CSV files.  
The API allows users to retrieve temperature data **by station**, **by date**, and **by year**, and also provides a simple homepage listing available stations.

---

## 📌 Project Overview

This project is built to demonstrate:
- Building REST-style APIs using **Flask**
- Reading and processing structured data with **Pandas**
- Serving JSON responses from CSV-based datasets
- Basic HTML templating using **Jinja2**

The application uses historical weather data stored in text files and exposes multiple endpoints to access this data programmatically.

---

## 🚀 Features

- Home page listing all available weather stations
- Retrieve temperature for a specific station on a specific date
- Retrieve all temperature data for a station
- Retrieve yearly temperature data for a station
- Automatic station ID formatting using zero-padding
- JSON-based API responses

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|------------|
| Language | Python |
| Framework | Flask |
| Data Processing | Pandas |
| Frontend | HTML (Jinja2 templates) |
| Data Source | CSV / TXT files |

---

## 📂 Project Structure

```text
Weather_API/
├── main.py                 # Flask application and API routes
├── templates/
│   ├── home.html           # Homepage with API usage instructions
│   └── about.html          # Static about page
├── data_small/             # Weather data files (stations and temperature records)
│   ├── stations.txt
│   └── TG_STAID******.txt
├── README.md
```

---

## ⚙️ Installation & Setup

git clone <repository_url><br>
cd Weather_API

python -m venv venv<br>
source venv/bin/activate      # Linux / macOS<br>
venv\Scripts\activate         # Windows

pip install flask pandas

---

## ▶️ Run the Application


Start the Flask development server by running:<br>
python main.py

