import streamlit as st
import functions

todos = functions.read_todos()



st.title('My Todo App')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")