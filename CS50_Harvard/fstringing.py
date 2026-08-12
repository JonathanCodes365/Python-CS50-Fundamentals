#Now, we are doing the f-strings.

#F-strings are very much important as they are widely used in AI/ML and programming to
#print  result ,debug and display model information.

#The format of using fstrings are simple:

# (f"{"String ,{ Variable }"})

#So, what can the variables be ?

#It can be  1. expressions 2.variables itself.

name = "Ngawang"
age = 20
number1 = 30
cost = 19.999

#so, when we are using f-string: we are telling that--> 
#hey, i am going into insert something special inside it and you better notice it.
print(f"Hello, My name is {name} and I am {age} years old")

#we can also insert expressions inside the f-strings.
print(f"I will be {age+number1} after 30 years")

#we can also use f-string to format decimal points.
print(f"Cost of 1 ticket is {cost:.2f}")
