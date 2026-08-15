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
#- Use loops this time
# Write your solution below:

numbers = [10, 20, 30, 40]
targets = [20, 30, 50, 60]

for target in targets:
    if target not in numbers:
        numbers.append(target)
print(numbers)