#Write a Python program that:
#	1.	Continuously asks the user to enter a number.
#	2.	If the user types “exit”, the program stops.
#	3.	If the number is even, print "AI: That’s an even number! ✅"
#	4.	If the number is odd, print "AI: That’s an odd number! 🔹"
#	5.	If the user enters something that isn’t a number, print "AI: Please enter a valid number!"

def checknumber(x):
    if x % 2 ==0:
        print("It is an even number😎")
    else:
        print("It is an odd number")

while True:
    num = input("Enter your number you want to check or(type exit to terminate the program)")
    if num.lower()== "exit":
        print("GOODBYE")
    break 


try:
    number = int(num)
    checknumber(number)
except ValueError:
        print("It shows value Error")
    
