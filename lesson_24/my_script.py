import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("Advertising_F.csv")
st.title("Advertising Dashboard by City Michael Frasketi")

st.sidebar.header("Filters")
x_var = st.sidebar.selectbox("X axis", ["TV", "radio", "newspaper"])

# show scatter plot
fig = px.scatter(
    df,
    x=x_var,
    y="sales",
    labels={
        "TV": "TV ad spend",
        "radio": "Radio ad spend",
        "newspaper": "Newspaper ad spend",
        "sales": "Sales",
    },
)
st.plotly_chart(fig)

# show the barplot
sales_per_city = df.groupby("City")["sales"].sum().reset_index()
fig = px.bar(sales_per_city, x="City", y="sales", title="data is fun")
st.plotly_chart(fig)

st.dataframe(df)
