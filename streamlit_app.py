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
st.write("""
This visualization shows the distribution of license statuses in the dataset. The most common status is "NOT RENEWED," followed by "ACTIVE," while the remaining statuses appear much less frequently. I chose a horizontal bar chart because it makes comparisons between different categories easier, especially when category names are relatively long. The x-axis uses a quantitative scale to represent the number of licenses, while the y-axis displays the categorical license statuses. I sorted the bars in descending order to highlight differences in frequency and used a consistent blue color to keep the chart simple and readable. If I had more time, I would group less common statuses into an "Other" category and improve the display of longer category labels.""")

st.header("Visualization 2: License Types by Status")

selected_status = st.selectbox(
    "Select a License Status",
    df["License Status"].unique()
)
filtered_df = df[df["License Status"] == selected_status]

type_counts = filtered_df["License Type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]

chart2 = alt.Chart(type_counts).mark_bar().encode(
    x="Count:Q",
    y=alt.Y("Type:N", sort = "-x", title="License Type"),
    tooltip=["Type", "Count"]
)

st.altair_chart(chart2, use_container_width=True)

st.write("""
This visualization explores how license types are distributed within different license statuses. Users can select a status from the dropdown menu, and the chart updates to display the corresponding license types and their counts. This interaction makes it possible to compare different subsets of the dataset without displaying all the information at once. I chose a horizontal bar chart because the license type names are relatively long, and sorting the bars by count makes the most common categories easier to identify. The x-axis represents the number of licenses, while the y-axis represents license types. I used the same blue color as the first visualization to maintain consistency between the two charts. If I had more time, I would add an option to display only the top ten license types and improve the readability of longer labels.""")

st.write("""
Both visualizations use a different dataset from Homework #5.
Neither the plots nor the analysis from Homework #5 were reused.
""")
