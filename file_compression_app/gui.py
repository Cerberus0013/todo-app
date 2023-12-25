import PySimpleGUI as pGui

label1 = pGui.Text("Select file to compress:")
input1 = pGui.Input()
choose_button1 = pGui.FilesBrowse("Choose")

label2 = pGui.Text("Select destination folder:")
input2 = pGui.Input()
choose_button2 = pGui.FolderBrowse("Choose")

window = pGui.Window("File Compressor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2]])


window.read()
window.close()