import pandas as pd
import numpy as np
import streamlit as st

header = st.container()
dataset = st.container()
eda = st.container()
model_training = st.container()


@st.cache_data
def get_data():
    df = pd.read_csv('HRDataset_v14.csv')
    return df 

with header:
    st.title('HR Analytics!!...')
    st.write(" ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write(" ")

with dataset:
    st.header('HR Dataset')
    st.text('This dataset is available from the Kaggle')
    st.write(get_data().head())
    st.write(" ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write(" ")

