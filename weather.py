import requests    
    
# Weather
def weather_get() :
    api_key = "acf573d894f4cf31c26e2a42909b12d2"
    city_name = "Dallas"
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")
    print("Todays forcast is ", description)
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    
    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
    
def main():
    weather_dict = weather_get
    print("Today's forcast is", weather_dict.get('description'))
    print("The minimum temp. is ", weather_dict.get('temp_min'))
    print("The max temp. is ", weather_dict.get('temp_max'))
    
main()