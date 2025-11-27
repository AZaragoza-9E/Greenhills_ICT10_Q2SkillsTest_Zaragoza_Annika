# Working with Dictionaries
from pyscript import display


weather_fortoday = {
    "location" : "Quezon City",
    "temperaturec_or_f" : 27,
    "humidity" : 80,
    "condition" : "Mostly Cloudy",
}

weather_fortoday['condition'] = 'Raining'
weather_fortoday['heatindex'] = 0  

display(weather_fortoday, target='weather')

display(f'We are currently in {weather_fortoday['location']}.', target='weather')
display(f'The temperature is currently {weather_fortoday['temperaturec_or_f']}°C.', target='weather')
display(f'The humidity is {weather_fortoday['humidity']}%.', target='weather')
display(f'The weather was mostly cloudy but is now {weather_fortoday['condition']}.', target='weather')
display(f'The heat index is {weather_fortoday['heatindex']}(Low).', target='weather')