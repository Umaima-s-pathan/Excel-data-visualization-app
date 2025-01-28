# -*- coding: utf-8 -*-
"""excel data visualization app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vckgLMEnaGFJnNGxF-BHQYjvXqRfFIsK
"""

import streamlit as st
import pandas as pd
import openai
import openpyxl
import matplotlib.pyplot as plt
import plotly.express as px

# Set the title of the app
st.title("Excel Data Visualization App")

# Sidebar for API Key input
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# File uploader for Excel files
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx","csv"])

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    st.write("Data Preview:", df)

    # Select a column for visualization
    column_to_plot = st.selectbox("Select a column to visualize", df.columns)

    # Visualization options
    plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    if st.button("Generate Plot"):
        if plot_type == "Line Chart":
            st.line_chart(df[column_to_plot])
        elif plot_type == "Bar Chart":
            st.bar_chart(df[column_to_plot])
        elif plot_type == "Scatter Plot":
            st.write("Scatter Plot")
            fig = px.scatter(df, x=df.index, y=column_to_plot, title=f'Scatter Plot of {column_to_plot}')
            st.plotly_chart(fig)

# Function to generate insights using OpenAI
def generate_insights(data):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Analyze this data: {data}"}]
    )
    return response.choices[0].message['content']

# Button to generate insights
if st.button("Generate Insights"):
    insights = generate_insights(df.to_dict())
    st.write("Insights from OpenAI:", insights)

