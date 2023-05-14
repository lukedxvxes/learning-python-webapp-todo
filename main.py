import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"]
    functions.add_todo(new_todo)
    st.session_state["new_todo"] = ""


todos = functions.read_todos()

st.title('My Todo App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        functions.complete_todo(index)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              placeholder="Enter a todo",
              on_change=add_todo,
              key="new_todo")
