# PRE-REQUISITES - 
# 1. Install requests module in python using the command "pip install requests"
# 2. Get your API Key from "https://aqicn.org/api/vn/"

import requests

# Function to retrive AQI
def aqi_checker(city_name) :
    
    api_key = "561aeff8e2fc76f3235dffdf50c40671b9a09007"
    url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve AQI data from the response
        aqi_data = response.json()
        aqi = aqi_data['data']['aqi']
        return aqi
    else:
        return "Failed to retrieve AQI data"

# Time retrival code 
def getTime(city_name) :
    api_key = "561aeff8e2fc76f3235dffdf50c40671b9a09007"
    url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"

    response = requests.get(url)
    time_data = response.json()
    time = time_data['data']['time']['s']

    return time

# Driver Code

city = input("Enter city name : ")
aqi_val = aqi_checker(city)
time_val = getTime(city)

# AQI Classification
if (aqi_val >= 0 and aqi_val <= 50) :
    classification = "Good"
elif (aqi_val > 50 and aqi_val <= 100) :
    classification = "Moderate"
elif (aqi_val > 100 and aqi_val <= 200):
    classification = "Unhealthy for Sensitive Groups"
elif (aqi_val > 200 and aqi_val <= 300):
    classification = "Unhelathy"
elif (aqi_val > 300 and aqi_val <= 400):
    classification = "Very Unhealthy"
elif (aqi_val > 400 and aqi_val <= 500):
    classification = "Hazardous"

# Output
print("City : ", city)
print("Date and Time : ", time_val)
print("AQI : ", aqi_val)
print("Category : ", classification)
