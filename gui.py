import functions
import time
import PySimpleGUI as pGui

pGui.theme("LightBlue7")

clock_label = pGui.Text("", key="clock")
label = pGui.Text("Type a todo")
input_box = pGui.InputText(tooltip="Enter to do", key="todo")
add_button = pGui.Button("Add")
list_box = pGui.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = pGui.Button("Edit")
complete_button = pGui.Button("Complete")
exit_button = pGui.Button("Exit")

window = pGui.Window("My todo app",
                     layout=[[clock_label],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button], [exit_button]],
                     font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                edit_todo = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                pGui.popup("Please select an item first")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(value=todos)
                window["todo"].update(value="")
            except IndexError:
                pGui.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todos"].update(value=values['todos'][0])
        case pGui.WIN_CLOSED:
            break
window.close()
