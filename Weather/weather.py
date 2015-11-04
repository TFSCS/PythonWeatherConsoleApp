import json
import urllib.request

print ("===================================================")
print ("TFS COMPUTER SCIENCE CLUB PYTHON WEATHER APP v0.1.0")
print ("===================================================")
print ("\n\n\n\n")
  

zip = (input("Enter Your Zip Code: ")) # Get Zipcode
API_KEY = open('API_KEY.txt', encoding="utf-8").read() # Past API KEY in text file within this directory.
apiURL = 'http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/' + zip + '.json' # apiURL Builder

# JSON Parser
with urllib.request.urlopen(apiURL) as url:
    response = url.read()
charset = url.info(). get_content_charset('utf-8')  # UTF-8 Encode
json_string = json.loads(response.decode(charset))
parsed_json = json_string


# Parsed Variables (Temp, Humidity, Conditions)
location = str(parsed_json['location']['city'])
weather = str(parsed_json['current_observation']['weather'])
currentTempF = str(parsed_json['current_observation']['temp_f'])
cuttentFeelsLikeTempF = str(parsed_json['current_observation']['feelslike_string'])
currentRelativeHumidity = str(parsed_json['current_observation']['relative_humidity'])

print ('===================================================')
print ('Weather For: ' + location )
print ('===================================================')
print ('Weather: ' + weather)
print ('Current Temperature: ' + currentTempF)
print ('Feels Like: ' + cuttentFeelsLikeTempF)
print ('Humidity: ' + currentRelativeHumidity)




