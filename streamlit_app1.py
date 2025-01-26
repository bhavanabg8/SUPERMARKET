
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

data = pd.read_csv("Supermart_dataset.csv") 

total_sales = data['Sales'].sum()
total_discount = data['Discount'].sum()
total_profit = data['Profit'].sum()

st.subheader("Total Sales, Discount, and Profit")
st.write(f"**Total Sales**: {total_sales}")
st.write(f"**Total Discount**: {total_discount}")
st.write(f"**Total Profit**: {total_profit}")

category_sales = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = data.groupby('Category')['Profit'].sum().sort_values(ascending=False)

region_sales = data.groupby('Region')['Sales'].sum()
region_profit = data.groupby('Region')['Profit'].sum()

st.subheader("Sales by Category")
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, ax=ax1)
ax1.set_title("Sales by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Total Sales")
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

st.subheader("Profit by Region")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=region_profit.index, y=region_profit.values, ax=ax2)
ax2.set_title("Profit by Region")
ax2.set_xlabel("Region")
ax2.set_ylabel("Total Profit")
st.pyplot(fig2)

