import streamlit as stl
import functions


def add_todos():
    new_todo = stl.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_todos(todos)
    print(new_todo)


todos = functions.get_todos()

stl.title("My Todo App")
stl.subheader("This is a todo app")

count = 1
for todo in todos:
    stl.checkbox(todo, key=count)
    count = count + 1

stl.text_input(label="Todo Entry:", placeholder="Enter a Todo...", on_change=add_todos, key="new_todo")
