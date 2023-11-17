# Simple Todo List with GUI
# Made by Moewen-dev
# Version 1.0

# imports 
import pickle
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Test')],
    [sg.Input(key='-IN-')],
    [sg.Button('Read'), sg.Exit()]
]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()