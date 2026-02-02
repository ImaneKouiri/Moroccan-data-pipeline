# Moroccan Socio-Economic Data Pipeline

## Project Overview :
This project is a student-level data engineering pipeline built to process
and analyze socio-economic indicators for Morocco using public data from
the World Bank.

The goal of the project is to simulate how a junior data engineer ingests,
cleans, stores, and analyzes real-world public data using Python and PostgreSQL.

## Objectives : 
- Ingest raw public CSV data
- Clean and transform the data using Python
- Store structured data in a PostgreSQL database
- Perform analytical SQL queries
- Visualize trends using Python

## Data Source : 
- **World Bank Open Data**
- Country: Morocco
- Selected indicators:
  - Total population
  - GDP (current USD)
  - Unemployment rate
  - Life expectancy
  - Literacy rate

## Pipeline Architecture
Raw CSV (World Bank)
↓
Python Ingestion Script
↓
Data Cleaning & Transformation (Pandas)
↓
PostgreSQL Database
↓
SQL Analysis
↓
Python Visualization (Jupyter Notebook)

## Tools & Technologies
- Python
- Pandas, NumPy, Matplotlib
- PostgreSQL
- SQLAlchemy
- Conda (environment management)
- Git & GitHub
- Linux

## How to Run the Project

### 1. Create and activate environment: 
```bash
conda create -n moroccan-data-pipeline python=3.10
conda activate moroccan-data-pipeline
pip install -r requirements.txt
```
### 2. Run ingestion & cleaning: 
```bash
python scripts/ingest_data.py
```
### 3. Create database & tables
```bash
sudo -u postgres psql -f sql/create_database.sql
psql -U imane -d moroccan_data -f sql/create_table.sql
```
### 4. Load data into PostgreSQL
```bash
python scripts/load_postgres.py
```
### 5. Run analysis queries
```bash
psql -U imane -d moroccan_data -f sql/analysis_queries.sql
```
### 6. Open notebook
```bash
jupyter notebook notebooks/analysis.ipynb
```
## Notes
- Database credentials are used for local development only.
- PostgreSQL must be installed and running locally.
- This project focuses on data engineering fundamentals rather than production deployment.
