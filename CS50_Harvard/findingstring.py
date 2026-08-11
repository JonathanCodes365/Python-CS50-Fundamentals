#Say, we want to find the exact location of a text ...
#Say, i want to find the exact index Jackson is located at

name = "Hi, My name is Jackson ; son of Jacky , Jack the Reaper"

#to find what index Jackson is located --> we have the find operator.
#What find operator does is it says us the index of the first letter of the text
#we are looking for.

print(name.find("Jackson"))


#Note: In this sentence there are repetitive alphabets like ac --> Jackson , Jacky , Jack
#When we want to find the letter ac it will point to the first one it gets.
