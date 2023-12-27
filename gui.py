import functions

import PySimpleGUI as pGui

label = pGui.Text("Type a todo")
input_box = pGui.InputText(tooltip="Enter to do", key="todo")
add_button = pGui.Button("Add")
list_box = pGui.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = pGui.Button("Edit")
complete_button = pGui.Button("Complete")
exit_button = pGui.Button("Exit")

window = pGui.Window("My todo app",
                     layout=[[label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button], [exit_button]],
                     font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            edit_todo = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window[todos].update(value=values['todos'][0])
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(value=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case pGui.WIN_CLOSED:
            break
window.close()
