import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Interactive Sales Dashboard')
st.write('This dashboard will display different types of sales, from sales data and analysis.')

data = {
  'Year': [2010, 2011, 2012, 2013, 2014, 2015],
  'Region': ['North', 'South', 'East', 'West', 'Central'],
  'Sales Amount': [200, 210, 220, 230, 240, 250]
}
df = pd.DataFrame(data)

selected_year = st.slider('Select a year', min_value=2010, max_value=2015, value=2013)

fig, ax = plt.subplots()
ax.bar(filtered_df['Region'], filtered_df['Sales Amount'], color='skyblue')
plt.title(f'Sales in {selected_year}')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
st.pyplot(fig)
