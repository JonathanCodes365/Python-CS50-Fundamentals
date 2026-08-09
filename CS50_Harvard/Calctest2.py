#in the previous code ,we had to wait till we could exit from the program
#we also need to wait to see if the input was faulty or not.

def checkoperation(num1, num2 , operator):
    if operator == "+":
        print(f"The result is {num1+num2}")
    elif operator == "-":
        print(f"The result is {num1-num2}")
    elif operator == "/":
        if num2 ==0:
            print("Invalid choice for division. Cannot be done ")
        else:
            print(f"The Result is {num1/num2}")
    elif operator == "*":
        print(f"The result is {num1*num2}")
    else:
        print("INVALID OPERATION MODEL")


while True:
    #1st we ask for number1
    #terminate as soon as exit is hit
    #go to valueError section as soon as an faulty value is entered

    number1 = input("Enter a number you want to enter(or type exit to terminate the program)")
    if number1.lower() == "exit":
        print("OH! GOOD BYE ! HOPE TO SEE YOU SOON ")
        break

    try:
        num1 = float(number1)

    except ValueError:
        print("OH! invalid choice mate.")
        continue

    number2 = input ("Enter a number you want to enter for the second one (or type exit to terminate the program)")

    if number2.lower() == "exit":
       print("OH! GOOD BYE ! HOPE TO SEE YOU SOON ")
       break
    
    try:
        num2 = float(number2)

    except ValueError:
        print("You have entered an invalid choice")

        operator = input ("Please Enter the operator you want to use (+ , - , / , *)")

    checkoperation (num1, num2, operator)
    