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
    print("Tasks:")
    tasks_len = len(tasks)
    for task, i in tasks, len(tasks):
        print(i + ". " + task)

# Function for adding tasks
def add_task(task):
    tasks.append(task)

# Function to remove task
def remove_task():
    print("TODO: Remove Task")

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
            try:
                list_tasks()
                input()
                continue
            except:
                print("No tasks loaded")
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
        case 6:
            print("Bye")
            exit(0)