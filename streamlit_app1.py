import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

data = pd.read_csv("Supermart_dataset.csv") 

st.title("Top 7 Categories by Sales and Profit")

cities = data['City'].unique()
selected_city = st.selectbox("Select a city:", cities, key='city')

if st.button("Generate Plots"):
    filtered_data = data[data['City'] == selected_city]

    grouped_data = filtered_data.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

    top_7_sales = grouped_data.sort_values(by='Sales', ascending=False).head(7)
    top_7_profit = grouped_data.sort_values(by='Profit', ascending=False).head(7)

    fig1, ax1 = plt.subplots()
    ax1.bar(top_7_sales['Category'], top_7_sales['Sales'], color='skyblue')
    ax1.set_title("Top 7 Categories by Sales")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Sales")

    fig2, ax2 = plt.subplots()
    ax2.bar(top_7_profit['Category'], top_7_profit['Profit'], color='lightgreen')
    ax2.set_title("Top 7 Categories by Profit")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Profit")

    col1, col2 = st.columns(2)

    with col1:

        buf1 = BytesIO()
        fig1.savefig(buf1, format="png")
        buf1.seek(0)
        st.download_button(
            label="Download Sales Plot as PNG",
            data=buf1,
            file_name="top_7_categories_sales.png",
            mime="image/png"
        )

    with col2:
        st.pyplot(fig2)

        buf2 = BytesIO()
        fig2.savefig(buf2, format="png")
        buf2.seek(0)
        st.download_button(
            label="Download Profit Plot as PNG",
            data=buf2,
            file_name="top_7_categories_profit.png",
            mime="image/png"
        )
