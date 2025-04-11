"""
This project, built using the Preswald platform, analyzes a synthetic dataset titled "AI-Powered Job Market Insights".
It explores job trends across industries with a focus on AI adoption, salary, and job roles. 
We cleaned the data by removing outliers using the IQR method and visualized the frequency of job titles using an interactive Plotly bar chart. 
The app provides a quick, visual understanding of the most in-demand roles. 
It demonstrates basic data manipulation, visualization, and UI building within a low-code environment.
"""

import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("/Users/rahulpanchal/Desktop/Structured_Lab/data/ai_job_market_insights.csv")
text = "AI JOB MARKET INSIGHT"
# Remove outliers from Salary_USD using IQR
Q1 = df['Salary_USD'].quantile(0.25)
Q3 = df['Salary_USD'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Salary_USD'] >= (Q1 - 1.5 * IQR)) & (df['Salary_USD'] <= (Q3 + 1.5 * IQR))]

# Count occurrences of each job title
value_counts = df['Job_Title'].value_counts().reset_index()
value_counts.columns = ['Job_Title', 'Count']

# Create an interactive bar chart
fig = px.bar(
    value_counts,
    x='Job_Title',
    y='Count',
    title='Count of Each Job Title',
    labels={'Count': 'Count', 'Job_Title': 'Job Title'},
    color='Count',
    color_continuous_scale='Viridis'
)

# Customize layout
fig.update_layout(
    xaxis_title='Job Title',
    yaxis_title='Count',
    title_x=0.5,
    xaxis=dict(tickangle=-45)
)

# Show the plot in browser
fig.show()
