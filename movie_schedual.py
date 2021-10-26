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