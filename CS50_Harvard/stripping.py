#This might be one of the most important and easiest function in py.

name = "   Ngawang Sherpa         "

#as you can see there are whitespaces before the beginning and ending of a string.

#normally printing this name would be give us :    Ngawang Sherpa
#so we dont want that ... that's not so very attractive.

#so what we do is we use strip function

print(name.strip())

#Okay, but thats just weird right ? Noone will go inputting that many backspaces in
#a input variable

#Here's another sceanario
fullname = input("Enter your name ")
#we are assuming that sometimes a user might accidentally press one or 2 more whitespaces.
#we want to remove that.

print(fullname.strip())