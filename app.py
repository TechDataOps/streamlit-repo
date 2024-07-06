import streamlit as st

st.title("Welcome to my first Streamlit app")

name = st.text_input("Enter your name: ")

st.write(f"Hello, {name}")

st.write("Let's find out Greatest of Three Numbers") # Set Title of the webapp

choice1 = st.number_input('Enter First number') #Accepts a number input
choice2 = st.number_input('Enter Second number')
choice3 = st.number_input('Enter Third number')

string = f'Largest entered number is {max(choice1,choice2,choice3)}'

st.write(string)
