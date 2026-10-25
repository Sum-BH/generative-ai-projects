# Quickstart Guide

This guide explains how to run the Vehicle Telemetry Analytics Pipeline end-to-end.

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.10 or newer
- MySQL Server (local instance recommended)
- Power BI Desktop
- VS Code (recommended)

### Required Python Packages

numpy
pandas
scipy
sqlalchemy
pymysql
matplotlib

cpp

Install dependencies using:

```bash
pip install -r requirements.txt
Step 1 — Generate Synthetic Telemetry Data
Run the notebook:

notebooks/01_synthetic_telemetry_generation.ipynb
This step:

Generates realistic synthetic telemetry data

Writes CSV files into:

bash
data/incoming_telemetry/
This notebook is executed once to create source data.

Step 2 — Run Telemetry Analytics Pipeline
Run the notebook:
notebooks/02_vehicle_telemetry_analytics_pipeline.ipynb
This step performs:

Telemetry ingestion

Signal cleaning and normalization

Modular analytics processing

SQL database creation and table population

On successful execution, analytics tables are written to the configured MySQL database.

Step 3 — Verify SQL Tables
Connect to MySQL and run:

sql

USE telemetry_analytics_db;
SHOW TABLES;
Expected tables:

telemetry_operating_profile

telemetry_thermal_behavior

telemetry_environmental_profile

telemetry_actuation_statistics

telemetry_frequency_features

Step 4 — Connect Power BI
Open Power BI Desktop

Select Get Data → MySQL database

Enter:

Server: localhost

Database: telemetry_analytics_db

Authenticate using MySQL credentials

Select all analytics tables

Click Load

Refresh visuals to view insights

Notes
Data directories are intentionally excluded from version control

Sample outputs are provided for reference only

All telemetry data in this project is synthetically generated

The analytics pipeline is modular and extensible

Disclaimer
This project is intended for educational and demonstration purposes only.
All data is synthetic and does not represent real vehicles, systems, or field programs.

