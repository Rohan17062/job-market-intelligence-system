# Job Market Intelligence System

## Overview

This project simulates a real-world data monitoring system for job market analytics. Instead of performing analysis on a 
static dataset, the system is designed to mimic how data arrives over time, how it is processed, and how meaningful insights 
are continuously extracted.

The system integrates data ingestion, anomaly detection and visualization into a single workflow. As new job data is introduced, 
the system updates its internal state, detects unusual patterns, and reflects those changes in an interactive dashboard.

This project is inspired by real-world data systems where continuous data flow, monitoring, and timely insights are critical 
for decision-making.

---

## Problem Statement

In real-world scenarios, job market data is not static — it is continuously generated across platforms and changes over time. 
Organizations that rely on this data need to monitor trends and detect unusual patterns to make informed decisions.

However, most basic data analysis approaches operate on fixed datasets and fail to capture:

* How hiring demand evolves over time
* Sudden drops or spikes in job postings
* Shifts in demand across roles, industries, and experience levels

Without a system that tracks changes incrementally, important signals can be missed or identified too late. There is a clear 
need for a structured approach that not only analyzes data but also monitors it continuously.

---

## Objective

The objective of this project is to build a system that:

* Simulates real-world data ingestion in batches
* Maintains a historical view of incoming data
* Detects anomalies such as sudden drops or spikes
* Performs structured analysis across multiple dimensions
* Presents insights through a dynamic dashboard

---

## Methodology

The project is designed as a layered system where each component handles a specific responsibility.

---

### 1. Data Ingestion (Simulation Layer)

A master dataset (`ai_job_market.csv`) acts as the source of truth. Data is released in batches to simulate real-world 
scenarios where information arrives incrementally rather than all at once.

* Variable batch sizes introduce realistic fluctuations
* New data is appended over time
* System state evolves with each ingestion

---

### 2. Data Pipeline (Processing Layer)

Incoming data is processed and stored in a SQLite database.

* Duplicate entries are avoided using unique identifiers
* Each batch is assigned an ingestion timestamp
* Historical records are preserved for time-based analysis

This layer ensures that the system maintains consistency and traceability.

---

### 3. Alert System (Monitoring Layer)

An anomaly detection mechanism monitors changes between consecutive ingestion dates.

* Identifies significant **drops** and **spikes** in job postings
* Uses percentage-based thresholds for detection
* Stores alerts with type (DROP/SPIKE) and timestamp
* Prevents duplicate alert generation

This transforms the system from passive analysis into active monitoring.

---

### 4. Analysis Layer

The system performs structured analysis across key dimensions:

* Job roles
* Experience levels
* Industries
* Company sizes
* Salary trends

Each analysis is evaluated for:

* Overall dataset
* Most recent data

This enables both long-term trend understanding and short-term shift detection.

---

### 5. Visualization Layer (Power BI Dashboard)

An interactive Power BI dashboard presents the processed data and insights.

The dashboard includes:

* Hiring trends over time
* Role and industry distributions
* Salary comparisons
* Alert monitoring (drop/spike detection)

The dashboard reflects changes dynamically whenever new data is ingested and refreshed.

---

## Alerts Monitoring

A dedicated alert system tracks unusual changes in job postings.

* Alerts are generated for significant drops or spikes
* Each alert is stored with timestamp and type
* Historical alerts can be analyzed and visualized

This enables visibility into abnormal system behavior and supports monitoring use cases.

---

## Dashboard Highlights

The Power BI dashboard is structured to provide both overview and detailed insights:

* KPI cards for total jobs and alerts
* Time-based trend analysis
* Distribution of job roles and industries
* Salary insights across roles
* Alerts summary and history

The dashboard is designed to clearly communicate both trends and anomalies.

---

## Project Structure

```text id="1s7a2x"
job-market-intelligence-system/

├── src/                 # Python scripts (pipeline, alerts, analysis)
├── data/                # datasets (CSV files, database created at runtime)
├── dashboard/           # Power BI file
├── screenshots/         # dashboard previews
└── README.md
```

---

## How to Run the Project

1. Clone the repository

2. Set up the database:

```
python src/setup_db.py
```

3. Simulate data ingestion:

```
python src/data_release.py
```

4. Run pipeline, alerts, and analysis:

```
python src/runner.py
```

5. Open the Power BI dashboard:

* Update data source path if required
* Click **Refresh** to view updated insights

---

## Important Note

The system is not based on real-time streaming but operates on incremental updates. Each time new data is ingested, the 
database is updated and the dashboard reflects the latest state upon refresh.

This approach closely resembles real-world systems that rely on scheduled or event-based data refresh.

---

## Conclusion & Real-World Relevance

This project demonstrates how a simple dataset can be transformed into a monitoring system that tracks changes over time 
rather than just analyzing static data.

In real-world applications, similar systems are used to:

* Monitor incoming datasets in data pipelines
* Detect anomalies or unexpected changes
* Track evolving trends in dynamic environments

By combining ingestion, anomaly detection, and visualization, this project provides a practical representation of how modern 
data workflows operate.

---

## Tech Stack

* Python (Pandas, SQLite)
* SQL
* Power BI

---

## Final Note

This project focuses on building a structured and evolving data system rather than performing one-time analysis. It 
emphasizes how data changes over time and how systems can be designed to monitor, analyze, and visualize those changes 
effectively.

---
