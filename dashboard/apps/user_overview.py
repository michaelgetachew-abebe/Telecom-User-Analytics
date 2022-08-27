import os
import sys
sys.path.append(os.path.abspath(os.path.join('../../scripts')))
sys.path.append(os.path.abspath(os.path.join('../../data')))
import streamlit as st
import pandas as pd

def app():
    # Loading the various dataframes needed!!!
    original_df = pd.read_csv('../../data/Week1_challenge_data_source(CSV).csv')
    #clean_df = pd.read_csv('../../data/clened_data.csv')

    st.title("USER OVERVIEW PAGE")

    st.subheader("Data Introduction")
    st.markdown("This section gives an introduction to the telecommunication dataset which is about the customers of the TellCo company, in Republic of Pefkakia. In this section we will get a birds eyeview statistical decription of the dataset.")
    st.write(original_df)


    st.subheader("INSIGHTS ABOUT CUSTOMERS")
    st.markdown("This section gives insights about customers by aggreagting them into different categories in the dataset.")
    #st.write(original_df)