import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

def delete_todo():
    print(todo)

st.title("My todo app")
st.subheader("we gaan todos bijhouden")
st.write("Dit is de lijst")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="geef hier je todo",
              on_change=add_todo, key='new_todo')


st.session_state