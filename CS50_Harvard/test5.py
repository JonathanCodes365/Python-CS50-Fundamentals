#using loops
#giving inputs until the user types exit.

def checkname(user_name):
    print("Your name is ", user_name)

def checkage(user_age):
    print("Your age is ",user_age)

while True:
    name =input("Enter your name or type (exit) to terminate the program ")
    if name.lower() == "exit":
        break
    checkname(name)
    age = int(input("Please,Enter your age"))
    checkage(age)