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
    print("")

# Function for adding tasks
def add_task(task):
    tasks.append(task)