import streamlit as st
import pandas as pd

st.title("Hello World!")

st.text("this is using a text function!")

st.header("A header function is being used to separate sections! ")

df_fruit = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

df_fruit = df_fruit.set_index("Fruit")

st.dataframe(df_fruit.head())

st.text("the dataframe() function is used to display the loaded dataframe!")

# we create user interaction

st.multiselect("This is a multiselect function creating a pick list",["need","pass in a","list"])

st.multiselect("Pick fruit",list(df_fruit.index))

st.dataframe(df_fruit)

st.text("order matters in interaction")

