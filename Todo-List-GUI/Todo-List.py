# Simple Todo List with GUI
# Made by Moewen-dev
# Version 1.0

# imports 
import pickle
import PySimpleGUI as sg

sg.theme('DarkAmber')

# Window layout
print("TODO: Get the layout right")
layout = [
    [sg.Text('Test')],
    [sg.Input(key='-IN-')],
    [sg.Button('Read'), sg.Exit()]
]

# Add task to tasks list
def add_task(task):
    print("TODO: add_task(task)")

# Remove task from tasks list
def remove_task(taskID):
    print("TODO: remove_task(taskID)")

# Save tasks to binary file
def save_tasks(tasks):
    print("TODO: save_tasks(tasks)")

# Load tasks from binary file
def load_tasks():
    print("TODO: load_tasks()")

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()