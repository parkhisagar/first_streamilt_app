
import streamlit as st
import pandas as pd

st.title('My Parents New Healthy Diner')
st.subheader('Breakfast Favorites')
st.write(' 🥣 Omega 3 & Blueberry oatmeal')
st.write(' 🥗 Kale, spinach & rocket smoothie')
st.write(' 🐔 Hard-boiled Free-Range egg')
st.write(' 🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

