import requests
BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "bef823d8b25a23e5171b766b892cad8f"
CITY =input("Enter your city")
url = BASE_URL +"appid=" + API_KEY + "&q=" +CITY
response =requests.get(url).json()
print(response)
print("Current Temperature ",response["main"]["temp"])
print("Current Temperature Feels like ",response["main"]["feels_like"])
print("Maximum Temperature ",response["main"]["temp_max"])
print("Minimum Temperature ",response["main"]["temp_min"])