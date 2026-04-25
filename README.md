# Job Market Data Pipeline & Anomaly Detection

## 🔹 Quick Summary

* Simulates **incremental job data ingestion** using batch processing
* Stores data in **SQLite with ingestion timestamp tracking**
* Detects **anomalies (job drop/spike)** using percentage-based logic
* Performs **trend analysis** across roles, industries, experience, and salary
* Visualizes insights and alerts using an **interactive Power BI dashboard**

---

## 📊 Dashboard Preview

![Overview](screenshots/overview.png)
![Trends](screenshots/trends.png)
![Alerts](screenshots/alerts.png)

---

## 🧠 Overview

This project builds a simplified version of a real-world data monitoring system.
Instead of analyzing a static dataset, it simulates how job data arrives over time and how systems process, monitor, and visualize that data continuously.

As new data is ingested, the system updates its internal state, detects unusual changes, and reflects those updates in a dashboard.

> The system is dynamic — dashboard insights change whenever new data is ingested and refreshed.

---

## ⚠️ Problem Statement

Job market data evolves continuously, but most analysis is performed on static datasets. This leads to:

* Missed changes in hiring trends over time
* No visibility into sudden drops or spikes in job postings
* Delayed or incomplete insights

There is a need for a system that not only analyzes data but also **monitors how it changes over time**.

---

## 🚀 Key Features

* Incremental data ingestion simulation
* Data pipeline with duplicate handling
* Timestamp-based tracking of data flow
* Anomaly detection (DROP/SPIKE alerts)
* Multi-dimensional trend analysis
* Interactive Power BI dashboard
* Alert storage and tracking system

---

## ⚙️ Methodology

### 1. Data Ingestion

* Uses a master dataset (`ai_job_market.csv`)
* Releases data in variable-sized batches
* Simulates real-world incoming data flow

### 2. Data Pipeline

* Processes incoming data and stores it in SQLite
* Prevents duplicate entries using `job_id`
* Tracks ingestion timestamps

### 3. Alert System

* Compares job counts between consecutive ingestion dates
* Detects:

  * **Drop** → significant decrease
  * **Spike** → sudden increase
* Stores alerts with type and timestamp
* Avoids duplicate alerts

### 4. Analysis Layer

* Evaluates trends across:

  * Job roles
  * Experience levels
  * Industries
  * Company size
  * Salary

* Compares **overall vs recent data**

### 5. Visualization

* Power BI dashboard displays:

  * Trends over time
  * Role and industry distribution
  * Salary insights
  * Alerts monitoring

---

## 🛠 Tech Stack

* **Python** (Pandas, SQLite)
* **SQL**
* **Power BI**

---

## 📁 Project Structure

```
job-market-data-pipeline/

├── src/                 # Python scripts
├── data/                # datasets (CSV + DB created at runtime)
├── dashboard/           # Power BI file
├── screenshots/         # dashboard previews
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

2. Setup database:

```
python src/setup_db.py
```

3. Simulate data ingestion:

```
python src/data_release.py
```

4. Run pipeline and analysis:

```
python src/runner.py
```

5. Open Power BI dashboard:

* Update data source path if needed
* Click **Refresh**

---

## ⚠️ Important Note

The dashboard is not real-time streaming but reflects **dynamic updates**.
Whenever new data is ingested and the dashboard is refreshed, all insights and alerts update accordingly.

---

## 🎯 Conclusion

This project demonstrates how to move from static data analysis to a **monitoring-based system** that tracks changes over time.

It reflects real-world use cases where:

* Data pipelines continuously ingest data
* Systems detect anomalies
* Dashboards support decision-making

---
