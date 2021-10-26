import requests

# Movie Schedual
current_movies = {'The Grinch':'11:00AM',
                  'Rudolph':"1:00PM", 
                  'Frosty the Snowman':'3:00PM',
                  'Christmas Vacation':'5:00PM'}

print("We're showing the following movies:")
for movie in current_movies:
    print(movie)
movies = input("What movie do you want the showtime for?\n")

showtime = current_movies.get(movies)
if showtime == None:
    print("Requested movie is'nt playing")
else:
    print(movies, " is playing at ", showtime)
    
# Contacts
contacts = {
    "number" :4,
    "students" :
        [
            {"name" : "Sarah Holderness", "email" : "sarah@example.com"},
            {"name" : "Harry Potter", "email" : "harry@example.com"},
            {"name" : "Bob Duncan", "email" : "bob@example.com"},
            {"name" : "Ron Wesley", "email" : "ron@example.com"}
        ]
}

for student in  contacts["students"]:
    print(student)
    print(student["email"])
    
# Weather Make it in a venv or virtual enviroment
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
