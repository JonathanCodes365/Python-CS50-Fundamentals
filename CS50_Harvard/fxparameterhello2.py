# here we want to send a parameter into the input of name


#to = "world " is us setting a default value when user doesnt give input in the hello()
def hello(to="world"):
    print("Hello",to)

hello()
name = input("What's your name ?")
hello(name)