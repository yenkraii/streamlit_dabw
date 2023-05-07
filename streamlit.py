import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# create a function
def get_fv_data(frch):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # standardise returned response to look prettier
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # streamlit.text(fruityvice_response.json())
  # to retreive the json response
  return fruityvice_normalized
  
  
st.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    st.error("Please select a fruit to get info")
  else:
    fvdt = get_fv_data(fruit_choice)
    # presenting it in a dataframe
    st.dataframe(fvdt)
    st.write('The user entered ', fruit_choice)
except URLError as e:
  st.error()

# connect to streamlit n retrieve the info imbued in the file


st.header("The fruit load list contains:")

# snowflake functions
def get_f_list():
  with conn.cursor() as cr:
    cr.execute("SELECT * from pc_rivery_db.public.fruit_load_list;")
    return cr.fetchall()

if st.button("Get Fruit Load List"):
  conn = snowflake.connector.connect(**st.secrets["snowflake"])
  dr = get_f_list()
  conn.close()
  st.dataframe(dr)

# allow insertion of data 

def insert_row(new_fruit):
  with conn.cursor() as cur:
    cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('"+ new_fruit +"');")
    return "Thanks for adding" + new_fruit

inp = st.text_input("What fruit would you like to add?","jackfruit")
if st.button("Add Fruit"):
  conn = snowflake.connector.connect(**st.secrets["snowflake"])
  t = insert_row(inp)
  conn.close()
  st.write(t)
