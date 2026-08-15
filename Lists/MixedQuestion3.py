# Problem: Add Only Missing Numbers
# You are given:
# numbers = [10, 20, 30, 40]
# targets = [20, 30, 50, 60]
# Your task is to add the target numbers that are NOT
# already present in numbers.
# Expected output:
# [10, 20, 30, 40, 50, 60]
# Requirements:
# - Use "in" or "not in".
# - Use append().
# - Do not manually add 50 and 60.
# Write your solution below:

numbers = [10, 20, 30, 40]
targets = [20, 30, 50, 60]
x=targets[0]
y=targets[1]
z=targets[2]
a=targets[3]

if x not in numbers:
    numbers.append(x)

if y not in numbers:
    numbers.append(y)

if z not in numbers:
    numbers.append(z)

if a not in numbers:
    numbers.append(a)


print(numbers)
