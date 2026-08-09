 #using functions to ask for name and age.

def checkname(user_name):
    print("Hello", user_name)

name = input("Enter your name.")
checkname(name)

def checkage(user_age):
    if user_age >=18:
        print("You are an adult with age of ", user_age)
    else:
        print("You are an minor with age",user_age)

age = int(input("Enter your age please."))
checkage(age)

