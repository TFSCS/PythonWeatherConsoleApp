import json
import urllib.request

print ("===================================================")
print ("TFS COMPUTER SCIENCE CLUB PYTHON WEATHER APP v0.1.0")
print ("===================================================")
print ("\n\n\n\n")
  

zip = (input("Enter Your Zip Code: "))

API_KEY = open('API_KEY.txt', encoding="utf-8").read()

apiURL = 'http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/' + zip + '.json'


# JSON Parser
with urllib.request.urlopen(apiURL) as url:
    response = url.read()
charset = url.info(). get_content_charset('utf-8')  # UTF-8 is the JSON defaultjson_string = f.json
json_string = json.loads(response.decode(charset))
parsed_json = json_string


# Parsed Variables (Temp, Humidity, Conditions)
location = parsed_json['location']['city']
currentTempF = parsed_json['current_observation']['temp_f']
cuttentFeelsLikeTempF = parsed_json['current_observation']['feelslike_string']
currentRelativeHumidity = parsed_json['current_observation']['relative_humidity']


print ('Current temperature in ' + str(location) + ' is: ' + str(currentTempF) + ' deg. F')



