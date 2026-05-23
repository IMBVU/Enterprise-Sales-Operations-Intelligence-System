
---

# Enterprise Sales & Operations Intelligence System

Enterprise analytics platform designed to centralize CRM, revenue, and operational datasets into automated KPI dashboards and executive reporting workflows for operational visibility and business performance tracking.

---

## Tech Stack

Python | Power BI | Snowflake | SQL | Airbyte | Power Automate | Streamlit

---

## Dashboard Preview

(Add dashboard screenshots or GIFs here)

---

## Business Problem

Organizations often struggle with disconnected CRM, sales, and operational data, limiting visibility into revenue performance, conversion efficiency, and operational bottlenecks.

---

## Solution

Built a centralized enterprise intelligence system integrating synthetic CRM and operational datasets into automated ETL pipelines, KPI dashboards, and reporting workflows to improve business visibility and executive decision-making.

---

## Key Features

- Automated ETL pipelines
- CRM analytics workflows
- Revenue performance dashboards
- Sales funnel analysis
- Conversion tracking
- Executive KPI reporting
- Automated operational alerts

---

## Architecture Overview

CRM / Sales Data
      ↓
Airbyte ETL Pipelines
      ↓
Snowflake Data Warehouse
      ↓
Power BI / Streamlit Dashboards
      ↓
Power Automate Reporting Workflows

---

## KPI Metrics

- Revenue Growth
- Pipeline Conversion Rate
- Sales Performance
- Operational Efficiency
- Customer Acquisition Trends
- Regional Business Performance

---

## Repository Structure

/data
/dashboard_app
/sql
/etl
/assets
/docs

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Enterprise-Sales-Operations-Intelligence-System.git
cd Enterprise-Sales-Operations-Intelligence-System

Create Virtual Environment

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Dashboard
streamlit run app.py
