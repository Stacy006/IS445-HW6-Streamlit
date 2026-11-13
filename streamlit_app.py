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

st.header("Visualization 2: License Types by Status")

selected_status = st.selectbox(
    "Select a License Status",
    df["License Status"].unique()
)
filtered_df = df[df["License Status"] == selected_status]

type_counts = filtered_df["License Type"].value_counts().reset_index()
type_counts.columns = ["License Type", "Count"]

chart2 = alt.Chart(type_counts).mark_bar().encode(
    x="Count:Q",
    y=alt.Y("Licnese Type:N", sort = "-x"),
    tooltip=["License Type", "Count"]
)

st.altair_chart(chart2, use_container_width=True)

st.write("""
This visualization shows the distribution of license statuses in the dataset. A horizontal bar chart was chosen to make comparisons between categories easier. The bars are sorted by count, allowing the most common statuses to be identified quickly. If more time were available, I would improve the chart by grouping less common statuses together to reduce visual clutter.
""")
