# Decades
age = int(input("How old are you?\n"))  #input taken will be a str so we need to turn it to int
decades = age // 10       #Gets whole number instead of 2.2
years = age % 10          #Gets remainder
print("You are " + str(decades) + " decades and " + str(years) + " years old") #need to turn it back to strin to concatnate