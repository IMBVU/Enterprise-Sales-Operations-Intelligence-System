-- Snowflake schema for Enterprise Sales & Operations Intelligence System
CREATE OR REPLACE TABLE accounts (account_id STRING, account_name STRING, industry STRING, region STRING, segment STRING, employee_count NUMBER, created_date DATE);
CREATE OR REPLACE TABLE opportunities (opportunity_id STRING, account_id STRING, created_date DATE, expected_close_date DATE, sales_rep STRING, region STRING, industry STRING, segment STRING, lead_source STRING, stage STRING, amount NUMBER, probability FLOAT, sales_cycle_days NUMBER, weighted_pipeline NUMBER);
CREATE OR REPLACE TABLE sales_activities (activity_id STRING, opportunity_id STRING, activity_type STRING, activity_date DATE, status STRING, owner STRING);

CREATE OR REPLACE VIEW sales_kpi_summary AS
SELECT region, segment, stage, COUNT(*) AS opportunities, SUM(amount) AS pipeline_value, SUM(weighted_pipeline) AS weighted_pipeline, AVG(sales_cycle_days) AS avg_cycle_days
FROM opportunities
GROUP BY region, segment, stage;
