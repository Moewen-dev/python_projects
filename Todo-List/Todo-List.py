# Simple Todo List
# Made by Moewen-dev
# Version 1.0

# imports
import os

# Initialize an empty list of tasks
tasks = []

# Main Menu
def print_main_menu():
    print("""
------------Main Menu------------
| 1. List all Tasks             |
| 2. Add Task                   |
| 3. Remove Task                |
| 4. Safe Tasks to File         |
| 5. Load Tasks from File       |
| 6. Exit                       |
---------------------------------""")

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for listing all current tasks
def list_tasks():
    tasks_len = len(tasks)
    if tasks_len == 0:
        print("No Tasks Loaded")
    elif tasks_len == 1:
        print("Tasks:")
        print("1. "+ tasks[0])
    else:
        i = 0
        print("Tasks:")
        while (i < tasks_len):
            ctask = i + 1
            print(str(ctask) + ". " + tasks[i])
            i += 1

# Function for adding tasks
def add_task(task):
    tasks.append(task)

# Function to remove task
def remove_task(task_nr):
    tasks.pop(task_nr - 1)

# Function to save tasks to a File
def save_tasks():
    print("TODO: Save Tasks")   

# Function to load tasks from file
def load_tasks():
    print("TODO: Load Tasks")

# Main Loop
while (True):
    clear_screen()
    print_main_menu()
    print("Option: ", end="")
    try:
        menu_input = int(input())
    except:
        print("Please enter a valid input")
        input()
        continue
    match menu_input:
        case 1:
            list_tasks()
            input()
            continue
        case 2:
            print("Enter new task:", end="")
            new_task = input()
            if new_task == '':
                print("Invalid Input!")
                input()
                continue
            add_task(new_task)
            input()
            continue
        case 3:
            print("Enter the task number of the task that you want to delete.")
            print("Number: ", end="")
            try:
                dtask = int(input())
                remove_task(dtask)
                print("Deleted Task: " + str(dtask))
                input()
                continue
            except:
                print("Invalid Input")
                input()
                continue
        case 6:
            print("Bye")
            exit(0)