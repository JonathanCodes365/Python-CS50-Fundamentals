def checkoperator (num1, num2 , operator):
    if operator == "+":
        print(f"The result is {num1+num2}")
    elif operator == "-":
        print(f"The result is {num1-num2}")
    elif operator == "/":
        if num2 == 0:
            print("Invalid number we cannot divide")
        else:
            print(f"The result is {num1/num2}")
    elif operator == "*":
        print(f"The result is {num1 *num2}")
    else:
        print("INVALID CHOICE")

while True:
    number1 = input("Enter number1 or (type exit to terminate the program)")
    number2 = input("Enter number2 or (type exit to terminate the program)")
    
    if number1.lower() == "exit" or number2.lower() == "exit":
        print("Goodbye! SEE YOU SOON MATE")
        break

    operator = input("Enter the operator you want to use ( + , - , /, *)")
    
    try:
        num1 = float(number1)
        num2 = float(number2)
        print("You have decided to operate on {num1} and {num2}")
        checkoperator (num1, num2, operator)

    except ValueError:
        print("You have entered an invalid choice")

                     