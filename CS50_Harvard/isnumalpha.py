#We have functions like isalpha , isnum and isalnum to check the type of input given.
#So, the output is either true or false.

#and as by the name we can see isalpha means if the string is completely alphabetical.
#isdigit means: if the given string is number or not.
#isalnum: means if the digit is number and a string or not.
#For example:

name =input("Enter your name")
if name.isalpha():
    print(f"Your name is {name}")
else:
    print("Enter alphabets only lowkey!!")
#but this above code has a problem.
#since .isalpha checks and gives true value if the input is only alphabets.
#so one might enter fullname .. there is bound to be a space.

#so we can do
fullname = input("Enter your full name")
y = fullname.replace(" ", "")
if y.isalpha():
    print(f"Your name is {fullname} ")
else:
    print("Please, Enter a valid name.")

age =input("Enter your age")
if age.isdigit() and  0<int(age)<100:
    print(f"Your age is {age}")
else:
    print("Please:Use numerics only or enter a valid age. ")

#ok the next fun part is we might need usernames in facebook , ig , discord and all other regions.
#there we use alphanumerics meaning we might need to use both alphabets and numerics.

#so,
username = input("Enter your username")
y = username.replace(" ", "")
if y.isalnum:
    print(f"Your username is {username}")
else:
    print("Enter valid username")



