import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA Disaster Relief Dashboard")
st.write("Author: YOUR NAME")

# Load data
df = pd.read_csv("fema_cleaned.csv")

st.subheader("Data Preview")
st.write(df.head())

# Histogram
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(
    df,
    x="repairAmount",
    nbins=40,
    title="Distribution of Repair Amounts"
)
st.plotly_chart(fig_hist)

# Boxplot
st.subheader("Repair Amount by TSA Eligibility")
fig_box = px.box(
    df,
    x="tsaEligible",
    y="repairAmount",
    title="Repair Amount by TSA Eligibility",
    labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)"}
)
st.plotly_chart(fig_box)

# Insight
st.markdown("""
### Insight
TSA-eligible households tend to show higher repair amounts, which makes sense because FEMA prioritizes households with more severe damage.
""")
