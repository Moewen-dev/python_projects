# Simple CLI Weather App
# Version 1.0.0
# Made by Moewen-dev

# imports
import dotenv
import requests
import json
import configparser

Config = configparser.ConfigParser()
Config.read("./config.ini")


# Configparser helper function
def config_section_map(section):
    dict1 = dict()
    options = Config.options(section)
    for option in options:
        dict1[option] = Config.get(section, option)
    return dict1
        

# the Main Menu
def menu():
    print("""
    ----------------Main-Menu----------------
    | 1. Display Current Weather Data       |
    | 2. Show and/or Edit Config
    |
    |
    """)


# Get the current weather data for a given location
def get_weather(location):
    print("Todo: get_weather(location)")
    

# Main Loop
def main():
    while True:
        print(config_section_map("general"))
        print("Todo: main()")
        break


main()
exit(0)
