import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"]
    functions.add_todo(new_todo)


todos = functions.read_todos()

st.title('My Todo App')

for todo in todos:
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        print(todo + ' completed')

st.text_input(label="Enter a todo",
              placeholder="Enter a todo",
              on_change=add_todo,
              key="new_todo")

st.session_state