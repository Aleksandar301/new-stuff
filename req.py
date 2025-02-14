import requests
import json

# API key
api_key = "http://api.open-notify.org/iss-now.json"

# response code and message
response = requests.get(api_key)
message = response.json()

# show the response code 
print("Response code is: ", response)
print(message)

# file to which the data shall be written
out_file = open("data.json", "w")

# writing the data insto the json file
json.dump(message, out_file, indent = 6)
