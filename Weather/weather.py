#Copyright 2015 All Rights Reserved. Tallulah Falls Computer Science. GPLv2
#This source file is free software, under the terms of the GNU GPLv2 General Public License.
import json
import urllib.request
import os
import sys

# Create and format API URL
API_KEY = open('API_KEY.txt', encoding="utf-8").read() # Paste API KEY in text file within this directory.
if '<insert your api key here>' in API_KEY:
    print ('ERROR: Place your api key in the "API_KEY.txt" file')
    sys.exit()

# Clears the console and prints header
def printHeader():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("|====================================================================")
    print ("|TFS COMPUTER SCIENCE PYTHON WEATHER APP v0.1.0")
    print ("|====================================================================")
printHeader()# execute

# Get selection of inputting either a zip code or a city.
print ("Please select whether to use a zip code or city")
print ("1) Zip \n2)City\n")
selection = (input(""))

#Clear console
printHeader()

# Set global API URL
global apiURL
    
# Creating API URL based on the selection
if selection == "1":
    zip = (input("Enter Your Zip Code: "))
    printHeader()
    apiURL = 'http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/' + zip + '.json' # apiURL Builder
elif selection == "2":
    city = (input("|Enter Your City: "))
    printHeader()
    state = (input("|Enter Your State or Country: "))
    printHeader()
    apiURL = 'http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/' + state + '/' + city + '.json' 

# Fetch and parse JSON
with urllib.request.urlopen(apiURL) as url:
    response = url.read()
charset = url.info(). get_content_charset('utf-8')  # UTF-8 Encode
json_string = json.loads(response.decode(charset))
parsed_json = json_string

# Check for an invalid zip code input
if 'No cities match your search query' in str(response):
    print ('ERROR: INVALID LOCATION')
    sys.exit()

# Parsed Variables (Temp, Humidity, Conditions)
locationFull = str(parsed_json['current_observation']['display_location']['full'])
weather = str(parsed_json['current_observation']['weather'])
temp = str(parsed_json['current_observation']['temperature_string'])
feelsLikeTemp = str(parsed_json['current_observation']['feelslike_string'])
relativeHumidity = str(parsed_json['current_observation']['relative_humidity'])
pressure = str(parsed_json['current_observation']['pressure_in'])
visibilityM = str(parsed_json['current_observation']['visibility_mi'])
windM = str(parsed_json['current_observation']['wind_mph'])

# Output
printHeader()
print ('|Weather For: ' + locationFull )
print ("|====================================================================")
print ('|Weather: ' + weather)
print ('|Temperature: ' + temp)
print ('|Feels Like: ' + feelsLikeTemp)
print ('|Humidity: ' + relativeHumidity)
print ('|Pressure: ' + pressure)
print ('|Visibility: ' + visibilityM)
print ('|Wind Speed: ' + windM)