location = input('Where in the world are you?')

import requests

r = requests.get('https://www.metaweather.com/api/location/search/?query')

#TO DO:
# 1) Ask user what city they are in.
# 2) Get city name to get WOEID(where on earth ID).
# 3) Use WOEID to get weather data.
# 4) Convert data from JSON text to python dictionary.
# 5) Loop over the dictionary and display the forecast for each day.
