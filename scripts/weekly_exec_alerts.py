import pandas as pd
opp = pd.read_csv("data/opportunities.csv")
summary = opp.groupby("region").agg(pipeline=("amount","sum"), weighted=("weighted_pipeline","sum"), avg_cycle=("sales_cycle_days","mean"), opps=("opportunity_id","count")).reset_index()
summary["alert"] = summary.apply(lambda r: "Review cycle time" if r.avg_cycle > 75 else "On track", axis=1)
print(summary.sort_values("weighted", ascending=False).to_string(index=False))
