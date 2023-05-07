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

st.multiselect("This is a multiselect function creating a pick list",["need","pass in a","list","pre-entered"], ["pre-entered","list"])

filtered = st.multiselect("Pick fruit",list(df_fruit.index))
df_filtered = df_fruit.loc[filtered]

st.dataframe(df_filtered)

st.text("need to save selection as a variable to be used to loc[] out the relevant rows")
st.text("then display the filtered dataframe instead")

#New section to utilise fruityvice api response

# streamlit.text(fruityvice_response.json())
# to retreive the json response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# standardise returned response to look prettier
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# presenting it in a dataframe
streamlit.dataframe(fruityvice_normalized)
