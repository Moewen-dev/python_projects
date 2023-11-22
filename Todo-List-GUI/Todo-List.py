# Simple Todo List with GUI
# Made by Moewen-dev
# Version 1.0

# imports 
import pickle
import PySimpleGUI as sg

sg.theme('DarkAmber')

cprint = sg.cprint

MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY

output_key = MLINE_KEY

# Window layout
print("TODO: Get the layout right")
layout = [
    [sg.Button('Add Task'), sg.Button('Remove Task')],
    [sg.Multiline(size=(50, 20),
                  auto_size_text=True,
                  auto_refresh=True,
                  no_scrollbar=True,
                  key=MLINE_KEY
                  )],
    [sg.B('Save'), sg.B('Load'), sg.Exit('Exit')]
]

# Initialise the tasks list
tasks = list()


# Add task to tasks list
def add_task(task):
    tasks.append(task)


# Remove task from tasks list
def remove_task(task_id):
    try:
        task_id = int(task_id)
    except ValueError:
        sg.popup_error_with_traceback('Invalid Input:\n')
    tasks.pop(task_id - 1)


# Save tasks to binary file
def save_tasks(tasklist):
    with open('taskfile', 'wb') as fp:
        pickle.dump(tasklist, fp)


# Load tasks from binary file
def load_tasks():
    with open('taskfile', 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list


window = sg.Window('Moewe´s Todo List', layout)

sg.cprint_set_output_destination(window, output_key)

while True:
    event, values = window.read()
    window[MLINE_KEY].update('')
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Task':
        add_task(sg.popup_get_text('Enter your task', title='Add Task'))
        print(tasks)
    if event == 'Remove Task':
        remove_task(sg.popup_get_text('Enter task ID', title='Remove Task'))
    if event == 'Save':
        save_tasks(tasks)
        sg.popup_auto_close('Saved Tasks to file', title='Saved', auto_close_duration=5)
    if event == 'Load':
        tasks = load_tasks()
        sg.popup_auto_close('Loaded Tasks from file', title='Loaded', auto_close_duration=5)
    for i in range(len(tasks)):
        cprint(f'{i + 1}. {tasks[i]}')
        i += i
window.close()
