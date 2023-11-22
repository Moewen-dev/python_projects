# Simple CLI Weather App
# Version 1.0.0
# Made by Moewen-dev

# imports
import dotenv
import requests
import json
import os
from datetime import datetime
import tzlocal

dotenv.load_dotenv("./.env")


# Clear the cli
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        

# the Main Menu
def menu():
    print("""
    ----------------Main-Menu----------------
    | 1. Display current weather data       |
    | 9. Exit                               |
    -----------------------------------------
    """)


# Get the current weather data for a given location
def get_weather(location):
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

    querystring = {"city": location}

    headers = {
        "X-RapidAPI-Key": os.environ["API_KEY"],
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.content


# Main Loop
def main():
    while True:
        clear_screen()
        menu()
        try:
            menu_choice = int(input("Option: "))
        except ValueError:
            print("Error: Invalid Input")
            input("Press Enter to continue")
            continue
        match menu_choice:
            case 1:
                clear_screen()
                location = input("Enter a Location \nLocation: ")
                current_time = datetime.now(tz=tzlocal.get_localzone()).strftime("%H:%M")
                current_time_long = datetime.now(tz=tzlocal.get_localzone()).strftime("%Y%m%d%H%M%S")
                weather_data = json.loads(get_weather(location))
                current_temp = weather_data["temp"]
                feels_like = weather_data["feels_like"]
                humidity = weather_data["humidity"]
                cloud_pct = weather_data["cloud_pct"]
                min_temp = weather_data["min_temp"]
                max_temp = weather_data["max_temp"]
                sunrise = datetime.fromtimestamp(weather_data["sunrise"],
                                                 tzlocal.get_localzone()).strftime("%H:%M")
                sunset = datetime.fromtimestamp(weather_data["sunset"],
                                                tzlocal.get_localzone()).strftime("%H:%M")
                weather = (f"""
Current Time: {current_time}
Current temp: {current_temp}°C
Feels like:   {feels_like}°C
Humidity:     {humidity}%
Cloud %:      {cloud_pct}%
Min temp:     {min_temp}°C
Max temp:     {max_temp}°C
Sunrise at:   {sunrise}
Sunset at:    {sunset}""")
                print(weather)
                print("\nDo you want to save the current weather to a txt file?")
                choice = input("Yes/No: ")
                if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
                    with open(f"Weather_{location}_{current_time_long}.txt", "w", encoding="utf-8") as weather_file:
                        weather_file.write(weather)
                    print(f"Saved as Weather_{location}_{current_time_long}.txt")
                input("\nPress Enter to get back to the main menu")
            case 9:
                input("Bye!")
                exit(0)


main()
exit(0)
