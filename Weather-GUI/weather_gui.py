# Weather App with Gui
# Made by Moewen-dev
# Version 1.0.1

# imports
import PySimpleGUI as sg
import requests
import json
import dotenv
import os
from datetime import datetime
import tzlocal

dotenv.load_dotenv('./.env')
sg.theme('DarkAmber')

col1 = [
    [sg.T('Location')],
    [sg.T('Current Date')],
    [sg.T('Current Time')],
    [sg.T('Weather Condition')],
    [sg.T('Temperature Now')],
    [sg.T('Feels Like')],
    [sg.T('Cloud Cover')],
    [sg.T('UV Index')],
    [sg.T('Humidity')],
    [sg.T('Rain Chance')],
    [sg.T('Rain Amount')],
    [sg.T('Visibility')],
    [sg.T('Wind Speed')],
    [sg.T('Wind Direction')],
    [sg.T('Wind Gusts')],
    [sg.T('Air Pressure')]
]

col2 = [
    [sg.T('', k='-LOCATION-')],
    [sg.T('', k='-CDATE-')],
    [sg.T('', k='-CTIME-')],
    [sg.T('', k='-WCONDITION-')],
    [sg.T('', k='-TNOW-')],
    [sg.T('', k='-FLIKE-')],
    [sg.T('', k='-CCOVER-')],
    [sg.T('', k='-UVINDEX-')],
    [sg.T('', k='-HUMIDITY-')],
    [sg.T('', k='-RCHANCE-')],
    [sg.T('', k='-RAMOUNT-')],
    [sg.T('', k='-VISIBILITY-')],
    [sg.T('', k='-WSPEED-')],
    [sg.T('', k='-WDIRECTION-')],
    [sg.T('', k='-WGUST-')],
    [sg.T('', k='-AIRPRESSURE-')]
]

layout = [
    [sg.B('Enter Location', k='-GET_LOCATION-')],
    [sg.Column(col1, visible=False, k='-COL1-'), sg.Column(col2, visible=False, k='-COL2-')],
    [sg.B('Get Weather', k='-GET_WEATHER-'), sg.B('Save', k='-SAVE-'), sg.Exit()]
]

window = sg.Window('Weather App', layout)


# Weather Api
def get_weather(location, units):
    api_key = os.environ['API_KEY']
    url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&units={units}&apikey={api_key}'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)
    return response.text


# Weather Code matching
def weathercode(wcode):
    all_codes = {
        "0": "Unknown",
        "1000": "Clear, Sunny",
        "1100": "Mostly Clear",
        "1101": "Partly Cloudy",
        "1102": "Mostly Cloudy",
        "1001": "Cloudy",
        "2000": "Fog",
        "2100": "Light Fog",
        "4000": "Drizzle",
        "4001": "Rain",
        "4200": "Light Rain",
        "4201": "Heavy Rain",
        "5000": "Snow",
        "5001": "Flurries",
        "5100": "Light Snow",
        "5101": "Heavy Snow",
        "6000": "Freezing Drizzle",
        "6001": "Freezing Rain",
        "6200": "Light Freezing Rain",
        "6201": "Heavy Freezing Rain",
        "7000": "Ice Pellets",
        "7101": "Heavy Ice Pellets",
        "7102": "Light Ice Pellets",
        "8000": "Thunderstorm"
    }
    return all_codes[wcode]


# Main
def main():
    global current_date, \
    current_time, \
    weather, \
    ctemp, \
    ctemp_feel, \
    cloud_cover, \
    uvindex, \
    humidity, \
    rain_prob, \
    rain_intensity, \
    visibility, \
    wind_speed_kph, \
    wind_direction, \
    air_pressure, \
    wind_gusts, \
    location

    while True:
        current_timedate = datetime.now(tz=tzlocal.get_localzone())

        event, value = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == '-GET_LOCATION-':
            location = sg.popup_get_text('Please enter you disiered location', title='Location Input')
            continue

        if location != '':
            weather_data = json.loads(get_weather(location, units='metric'))
            weather_values = weather_data['data']['values']
            current_date = current_timedate.strftime('%d.%m.%Y')
            current_time = current_timedate.strftime('%H:%M')
            ctemp = weather_values['temperature']
            ctemp_feel = weather_values['temperatureApparent']
            humidity = weather_values['humidity']
            wind_speed_mps = float(weather_values['windSpeed'])
            wind_speed_kph = float(wind_speed_mps) * 3.6
            wind_direction = weather_values['windDirection']
            wind_gusts = weather_values['windGust']
            air_pressure = weather_values['pressureSurfaceLevel']
            rain_intensity = weather_values['rainIntensity']
            rain_prob = weather_values['precipitationProbability']
            visibility = weather_values['visibility']
            cloud_cover = weather_values['cloudCover']
            uvindex = weather_values['uvIndex']
            wcode = weather_values['weatherCode']
            weather = weathercode(str(wcode))

        output = f'''Location: {location}
Current Date: {current_date}
Current Time: {current_time}
Weather: {weather}
Temp Now: {ctemp}°C
Feels Like: {ctemp_feel}°C
Cloud Cover: {cloud_cover}%
UV Index: {uvindex}
Humidity: {humidity}%
Rain Prob: {rain_prob}%
Rain Amount: {rain_intensity}mm/h
Visibility: {visibility}km
Wind Speed: {wind_speed_kph}km/h
Wind Direction: {wind_direction}°
Wind Gusts: {float(wind_gusts) * 3.6}km/h
Air Pressure: {air_pressure}hPa'''

        if event == '-GET_WEATHER-':
            if location != '':
                window['-COL1-'].update(visible=True)
                window['-COL2-'].update(visible=True)

                window['-LOCATION-'].update(location)
                window['-CDATE-'].update(current_date)
                window['-CTIME-'].update(current_time)
                window['-WCONDITION-'].update(weather)
                window['-TNOW-'].update(f'{ctemp}°C')
                window['-FLIKE-'].update(f'{ctemp_feel}°C')
                window['-CCOVER-'].update(f'{cloud_cover}%')
                window['-UVINDEX-'].update(uvindex)
                window['-HUMIDITY-'].update(f'{humidity}%')
                window['-RCHANCE-'].update(f'{rain_prob}%')
                window['-RAMOUNT-'].update(f'{rain_intensity}mm/h')
                window['-VISIBILITY-'].update(f'{visibility}km')
                window['-WSPEED-'].update(f'{int(wind_speed_kph)}km/h')
                window['-WDIRECTION-'].update(f'{wind_direction}°')
                window['-WGUST-'].update(f'{int(wind_speed_kph)}km/h')
                window['-AIRPRESSURE-'].update(f'{air_pressure}hPa')

        if event == '-SAVE-':
            date = current_timedate.strftime('%Y%m%d_%H%M')
            with open(f"./saves/Weather_{location}_{date}.txt", "w", encoding="utf-8") as weather_file:
                weather_file.write(output)
            sg.popup_ok(f'Saved as Weather_{location}_{date}.txt')


main()
