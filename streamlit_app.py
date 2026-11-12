import streamlit as st
import pandas as pd
import altair as alt

st.title("License Data Visualization")

df = pd.read_csv("licenses_fall2022.csv")

st.write("Dataset Preview")
st.dataframe(df.head())

st.header("Visualization 1: License Status Distribution")

status_counts = df["License Status"].value_counts().reset_index()
status_counts.columns = ["License Status", "Count"]

chart1 = alt.Chart(status_counts).mark_bar().encode(
    x="Count:Q",
    y=alt.Y("License Status:N", sort="-x"),
    tooltip=["License Status", "Count"]
)

st.altair_chart(chart1, use_container_width=True)
