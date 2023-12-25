import functions

import PySimpleGUI as pGui

label = pGui.Text("Type a todo")
input_box = pGui.InputText(tooltip="Enter to do")
add_button = pGui.Button("Add")
window = pGui.Window("My todo app", layout=[[label], [input_box, add_button]])
window.read()
window.close()
