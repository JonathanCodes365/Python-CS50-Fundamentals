# Problem: Check Before Adding
# You are given:
# numbers = [10, 20, 30, 40, 50]
# target = 30
# If target is NOT already in the list, add it using append().
# If it is already in the list, print:
# "Number already exists"
# Expected output:
# Number already exists
# Requirements:
# - Use "not in".
# - Use if/else.
# - Use append() only if the number isn't already present.
# Write your solution below:

numbers = [10, 20, 30, 40, 50]
target = 30
if target not in numbers:
    numbers.append(target)
else:
    print("Number already exists")