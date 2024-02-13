## Advanced Machine Learning Codealong: Introduction to Streamlit
## Week 3: Lecture 1
## Objectives:  
## Create streamlit app to explore a dataset
## Include: Visualize dataframe, print descriptive statistics, and Generate EDA plots of columns

## Reference: https://docs.streamlit.io/library/api-reference

## Import necessary packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px
import functions as fn


## load_data() with caching
@st.cache_data

def load_data():
    df = pd.read_csv('../Data/loan_approval.csv')
    return df
## TODO

## Global Variables

## Data
df = load_data()
## TODO

## Columns for EDA

## TODO

## Image, title and Markdown subheader
st.image('../Images/money_tree.jpg')
st.title('Loan Approval app')
st.markdown('Dataset from [kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)')
## TODO

## Display DataFrame
st.header('Loan Dataframe')
st.dataframe(df)
## TODO

## .info()
## Get string for .info()
buffer = StringIO()
df.info(buf = buffer)
info_text = buffer.getvalue()


## TODO

## Display .info()
st.sidebar.subheader('Summary')
s_text = st.sidebar.button('Info text')

if s_text:
    st.text(info_text)



## TODO

## Descriptive Statistics Subheader
st.sidebar.subheader('Descriptive statistics')


## TODO

## Button for Statistics

button_des = st.sidebar.button('Descriptive statistics')
if button_des:
    desc= df.describe()
    st.dataframe(desc)

## TODO

## Eda Plots subheader
st.sidebar.subheader('Explore a Column')

## TODO

## selectbox for columns

columns = df.columns
features = [col for col in columns if col != 'loan_status']
target = 'loan_status'

eda_column = st.sidebar.selectbox('Column to Explore', columns, index=None)

## Conditional: if column was chosen
if eda_column:
    ## Check if column is object or numeric and use appropriate plot function
    if df[eda_column].dtype == 'object':
        fig = fn.explore_categorical(df, eda_column)
    else:
        fig = fn.explore_numeric(df, eda_column)

    ## Show plot
    st.subheader(f'Display Descriptive Plots for {eda_column}')
    st.pyplot(fig)
## TODO

    
## Feature vs Target


feature_vs_target = st.sidebar.selectbox('Compare Feature to Target', features, index=None)

if feature_vs_target:
    ## Check if feature is numeric or object
    if df[feature_vs_target].dtype == 'object':
        comparison = df.groupby('loan_status').count()
        title = f'Count of {feature_vs_target} by {target}'
    else:
        comparison = df.groupby('loan_status').mean()
        title = f'Mean {feature_vs_target} by {target}'

    ## Display appropriate comparison
    pfig = px.bar(comparison, y=feature_vs_target, title=title)
    st.plotly_chart(pfig)
        