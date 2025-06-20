import streamlit as st
import random

fruit_names = ["Apple", "Apricot", "Banana", "Blackberry", "Blueberry", "Cantaloupe", "Cherry", "Date", "Dragon Fruit", "Fig", "Grape", "Grapefruit", "Kiwi", "Lemon", "Lime", "Mango", "Orange", "Papaya", "Peach", "Pear"]

weekly_fruits = random.sample(fruit_names, 7)

st.title("Weekly Fruit Picker")
st.write("Here are 7 fruits picked randomly for this week:")

for fruit in weekly_fruits:
    st.write(f"- {fruit}")
