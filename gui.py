import functions

import PySimpleGUI as pGui

label = pGui.Text("Type a todo")
input_box = pGui.InputText(tooltip="Enter to do", key = "todo")
add_button = pGui.Button("Add")
window = pGui.Window("My todo app",
                     layout=[[label], [input_box, add_button]],
                     font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
        case pGui.WIN_CLOSED:
            break
window.close()
