
import streamlit as st
import pandas as pd
import requests

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

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# bring in table with row column form with normalize
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# put it in dataframe
st.dataframe(fruityvice_normalized)

