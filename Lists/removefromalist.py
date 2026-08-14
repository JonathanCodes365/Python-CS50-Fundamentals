#next up after doing inserts..
#we are doing remove next

#As the name suggests; remove means = to remove something from a list

#Example:
numbers = [10,20,30,40,50]
numbers.remove(20)
print(numbers)

t1 = [10,20,20,30,40,50]
#if there are multiple numbers and we try to remove them, then only the first one that it meets is removed.
t1.remove(20)
print(t1)

#so what if we try to remove a number/string which is not on the list
#then we get ValueError.