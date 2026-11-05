
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("Advertising_F.csv")
st.title("Advertising Dashboard by City Michael Frasketi")

st.sidebar.header("Filters")
x_var = st.sidebar.selectbox("X axis", ["TV", "radio", "newspaper"])

# Show scatter plot dynamically based on user selection
fig_scatter = px.scatter(
    df,
    x=x_var,
    y='sales',
    color='City',
    labels={x_var: f'{x_var} Ad Spend', 'sales': 'Sales'},
    title=f'{x_var} Ad Spend vs Sales'
)
st.plotly_chart(fig_scatter)

# Show the barplot
sales_per_city = df.groupby("City")["sales"].sum().reset_index()
fig_bar = px.bar(sales_per_city, x='City', y='sales', title="Sales per City")
st.plotly_chart(fig_bar)

st.dataframe(df)
