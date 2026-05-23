# Power BI Dashboard Blueprint

Pages:
1. Executive KPI Scorecard: pipeline value, weighted pipeline, win rate, average deal size, sales cycle.
2. Funnel Performance: opportunity count by stage, conversion by lead source, closed-won revenue.
3. Sales Operations: rep productivity, open activities, blocked tasks, follow-up gaps.
4. Business Unit View: region, segment, industry, and lead-source filters.

Core DAX Measures:
Total Pipeline = SUM(opportunities[amount])
Weighted Pipeline = SUM(opportunities[weighted_pipeline])
Closed Won Revenue = CALCULATE(SUM(opportunities[amount]), opportunities[stage] = "Closed Won")
Win Rate = DIVIDE(CALCULATE(COUNTROWS(opportunities), opportunities[stage] = "Closed Won"), CALCULATE(COUNTROWS(opportunities), opportunities[stage] IN {"Closed Won", "Closed Lost"}))
Average Deal Size = AVERAGE(opportunities[amount])
Average Sales Cycle = AVERAGE(opportunities[sales_cycle_days])
