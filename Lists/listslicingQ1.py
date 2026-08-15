#List slicing is quite very much similar to that of String Slicing.

# Problem: Extract Element
# You are given:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Use slicing to print:
# [30, 40, 50, 60]
# Requirements:
# - Use slicing.
# - Do not use a loop.
# - Do not use individual indexes like numbers[2], numbers[3], etc.
# Write your solution below:

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:6])


# Problem: Select Every Second Element
# You are given:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Use slicing to produce:
# [10, 30, 50, 70]
# Requirements:
# - Use only slicing.
# - Do not use a loop.
# - Do not use individual indexes.
# Write your solution below:

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[::2])

#We must understand there's x, y and z in string slicing.

# z: represents how many index to jump... if we do 2 --> from 10(1 index) 20 (2nd index) to 30 
#we jump 2 indexes to reach 30 and so on.