
import streamlit as st
import pandas as pd
import requests
import snowflake.connector as sc
from urllib.error import URLError

st.title('My Parents New Healthy Diner')
st.subheader('Breakfast Favorites')
st.write(' 🥣 Omega 3 & Blueberry oatmeal')
st.write(' 🥗 Kale, spinach & rocket smoothie')
st.write(' 🐔 Hard-boiled Free-Range egg')
st.write(' 🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
   fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
     st.error("Please select a fruit to get information")
  else:    
     back_from_function = get_fruityvice_data(fruit_choice)
     st.dataframe(back_from_function)
except URLError as e:
    st.error()

#st.stop()
st.header("The fruit load list contains:")

def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

if st.button('Get Fruit Load List'):
   my_cnx = sc.connect(**st.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   st.dataframe(my_data_rows)
   
st.stop()

def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding - " + new_fruit

add_my_fruit = st.text_input('What fruit would you like to add?','Jackfruit')
if st.button('Add a new Fruit to List'):
   my_cnx = sc.connect(**st.secrets["snowflake"])
   back_from_function = get_fruityvice_data(fruit_choice)
   st.text(back_from_function)
   
# st.dataframe(add_my_fruit)

st.write('Thanks for adding - ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
