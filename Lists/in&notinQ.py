# Problem: Check for an Element
# You are given:
# numbers = [15, 27, 32, 41, 56, 73]
# Check whether 41 exists in the list.
# If it exists, print:
# "41 is present"
# Otherwise, print:
# "41 is not present"
# Requirements:
# - Use the "in" operator.
# - Use an if/else statement.
# Write your solution below:

numbers = [15, 27, 32, 41, 56, 73]
target = 41
if target in numbers:
    print('"41 is  present"')
else:
    print('"41 is not present"')