import streamlit as st
import pandas as pd

st.title("Hello World!")

st.text("this is using a text function!")

st.header("A header function is being used to separate sections! ")

df_fruit = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.dataframe(df_fruit)

st.text("the dataframe() function is used to display the loaded dataframe!")

