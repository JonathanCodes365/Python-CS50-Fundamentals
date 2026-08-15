# Problem: Reverse Every Second Element
# You are given:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Use slicing to produce:
# [80, 60, 40, 20]
# Requirements:
# - Use only slicing.
# - No loops.
# - No individual indexes.
# Write your solution below:

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
#we can use negative indexes for this 
print(numbers[-1:-8])
#but we must understand in here x:y:z
#by default z = +1 ; what we are saying here is this that start at -1 ; end at -7 but do +1 ?
#so we must also specify the step we need to do 
print(numbers[-1::-2])