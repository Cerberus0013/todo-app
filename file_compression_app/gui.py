import PySimpleGUI as pGui
import zip_creator as make_archive

label1 = pGui.Text("Select file to compress:")
input1 = pGui.Input()
choose_button1 = pGui.FilesBrowse("Choose", key="files")

label2 = pGui.Text("Select destination folder:")
input2 = pGui.Input()
choose_button2 = pGui.FolderBrowse("Choose", key="folder")

compress_button = pGui.Button("Compress")
output_label = pGui.Text(key="output")

window = pGui.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["files"].split(";")
    folder = values("folder")
    make_archive(filepath, folder)
    window["output"].update(value="Compression Completed")

window.close()