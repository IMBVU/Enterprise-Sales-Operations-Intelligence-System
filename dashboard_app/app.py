
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(page_title="Enterprise Sales & Operations Intelligence", page_icon="⚡", layout="wide")
ROOT = Path(__file__).resolve().parents[1] / "data"
opps = pd.read_csv(ROOT / "opportunities.csv", parse_dates=["created_date", "expected_close_date"])
acts = pd.read_csv(ROOT / "sales_activities.csv")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
.stApp {background: radial-gradient(circle at top left,#26115a 0%,#0b1020 35%,#020617 100%); color:#ecfeff; font-family:'Space Grotesk',sans-serif;}
.pulse {padding:2rem; border-radius:20px; background:linear-gradient(135deg,rgba(34,211,238,.18),rgba(168,85,247,.18)); border:1px solid rgba(125,211,252,.35); box-shadow:0 0 55px rgba(34,211,238,.12); animation:pulse 2.5s infinite;}
.pulse h1 {font-size:2.9rem; margin:0; letter-spacing:-.04em;}
.kpi {background:rgba(15,23,42,.78); border:1px solid rgba(34,211,238,.32); border-radius:18px; padding:1rem;}
.kpi span {font-family:'IBM Plex Mono',monospace; color:#67e8f9; font-size:.78rem; text-transform:uppercase;}
.kpi strong {display:block; font-size:1.9rem; margin-top:.2rem; color:#f0abfc;}
@keyframes pulse {0%,100%{box-shadow:0 0 35px rgba(34,211,238,.12)}50%{box-shadow:0 0 85px rgba(168,85,247,.22)}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='pulse'>
<h1>Enterprise Sales & Operations Intelligence System</h1>
<p>Neon executive operations dashboard for sales pipeline health, revenue forecasting, conversion performance, and activity efficiency across regions and business segments.</p>
</div>
""", unsafe_allow_html=True)

region = st.multiselect("Region", sorted(opps.region.unique()), default=sorted(opps.region.unique()))
segment = st.multiselect("Segment", sorted(opps.segment.unique()), default=sorted(opps.segment.unique()))
f = opps[opps.region.isin(region) & opps.segment.isin(segment)]

closed_won = f[f.stage.eq('Closed Won')]
win_rate = len(closed_won) / max(1, len(f[f.stage.isin(['Closed Won','Closed Lost'])]))
metrics = [
    ("Pipeline Records", f"{len(f):,}"),
    ("Total Pipeline", f"${f.amount.sum()/1_000_000:.1f}M"),
    ("Weighted Pipeline", f"${f.weighted_pipeline.sum()/1_000_000:.1f}M"),
    ("Win Rate", f"{win_rate:.1%}"),
]
cols = st.columns(4)
for col,(label,val) in zip(cols,metrics): col.markdown(f"<div class='kpi'><span>{label}</span><strong>{val}</strong></div>", unsafe_allow_html=True)

left,right = st.columns(2)
with left:
    st.subheader("Pipeline by Stage")
    stage = f.groupby('stage', as_index=False).agg(pipeline=('amount','sum'), opps=('opportunity_id','count'))
    st.altair_chart(alt.Chart(stage).mark_bar(cornerRadius=8).encode(x='pipeline:Q', y=alt.Y('stage:N', sort='-x'), tooltip=['stage','pipeline','opps']).properties(height=360), use_container_width=True)
with right:
    st.subheader("Revenue by Region")
    reg = f.groupby('region', as_index=False).agg(weighted_pipeline=('weighted_pipeline','sum'), avg_cycle=('sales_cycle_days','mean'))
    st.altair_chart(alt.Chart(reg).mark_circle(size=420).encode(x='avg_cycle:Q', y='weighted_pipeline:Q', color='region:N', tooltip=['region','weighted_pipeline','avg_cycle']).properties(height=360), use_container_width=True)

st.subheader("Monthly Pipeline Creation Trend")
monthly = f.assign(month=f.created_date.dt.to_period('M').astype(str)).groupby('month', as_index=False).agg(new_pipeline=('amount','sum'))
st.altair_chart(alt.Chart(monthly).mark_area(opacity=.7).encode(x='month:T', y='new_pipeline:Q', tooltip=['month','new_pipeline']).properties(height=320), use_container_width=True)

st.subheader("Automated Executive Alert")
open_pipe = f[~f.stage.str.contains('Closed')].weighted_pipeline.sum()
st.warning(f"Open weighted pipeline is ${open_pipe:,.0f}. Highest priority workflow: monitor late-stage proposals, follow-up activity volume, and region-level conversion gaps before forecast close.")
with st.expander("Preview opportunity data"):
    st.dataframe(f.head(500), use_container_width=True)
