import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    # place a string the local variable, and to get that string we need to refer to state
    # st.session_state["new_todo"] key = new_todo is the same line with
    # st.text_input(label="",placeholder="Add new..."
    #               on_change= add_todo, key='new_todo')
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # delete the to do also from session staten dictionary
        # so you can provide the to do as a key in st.session_state[tod.] that should delete the pair of selected from the state of dictionary
        del st.session_state[todo]
        #  st.experimental_rerun is to rerun the code
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change= add_todo, key='new_todo')



