import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st

data = pd.read_csv("c:/Users/Acer/Documents/PandasApp/Supermart_dataset.csv")
print(data.head())

data['Order Date'] = pd.to_datetime(data['Order Date'], format='%m/%d/%Y')

data = data.dropna()

summary = data[['Sales', 'Discount', 'Profit']].describe()

total_sales = data['Sales'].sum()
total_discount = data['Discount'].sum()
total_profit = data['Profit'].sum()

category_sales = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = data.groupby('Category')['Profit'].sum().sort_values(ascending=False)
category_discount = data.groupby('Category')['Discount'].sum().sort_values(ascending=False)

region_sales = data.groupby('Region')['Sales'].sum()
region_profit = data.groupby('Region')['Profit'].sum()

data['Year'] = data['Order Date'].dt.year
yearly_sales = data.groupby('Year')['Sales'].sum()
yearly_profit = data.groupby('Year')['Profit'].sum()


plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=region_profit.index, y=region_profit.values)
plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.show()


plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_sales.index, y=yearly_sales.values, label='Sales')
sns.lineplot(x=yearly_profit.index, y=yearly_profit.values, label='Profit')
plt.title('Sales and Profit Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



 
