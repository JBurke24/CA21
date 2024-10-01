import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Sales Dashboard")
st.write("""
This dashboard displays sales data analysis for different regions.
Use the slider to select a year range and click the "Show Analysis" button to see additional insights.
""")

year_range = st.slider("Select Year Range", 2010, 2020, (2010, 2020))
show_analysis = st.button("Show Analysis")

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East'],
    'Sales Amount': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
}

df = pd.DataFrame(data)

filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

st.write("Sales Data", filtered_df)

plt.figure(figsize=(10, 5))
plt.bar(filtered_df['Year'], filtered_df['Sales Amount'])
plt.title('Sales Amount by Year')
plt.xlabel('Year')
plt.ylabel('Sales Amount')
st.pyplot(plt)

if show_analysis:
    total_sales = filtered_df['Sales Amount'].sum()
    avg_sales = filtered_df['Sales Amount'].mean()
    st.write(f"Total Sales: {total_sales}")
    st.write(f"Average Sales: {avg_sales}")
