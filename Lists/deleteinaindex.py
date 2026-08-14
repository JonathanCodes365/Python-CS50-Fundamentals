#This is us doing delete in a list after doing pop
#delete where?
numbers = [10,20,30,40,50]
del numbers[2]
#we get numbers = [10,20,40,50]

#Heres a basic distinction between remove, pop and delete

# Remove is used to delete a number ... When someone says for example:
#Delete 30 from this list... you just do numbers.remove(30)

#But if some1 says to delete number from index 2.
# we do del numbers[2]

#if someone says delete that number from index 2 and also store it somewhere..
# x = numbers.pop(2)

#We can also do kindalike slicing .. meaning we can delete from a certain range
#remember during string operations we did 

#if
name = "Michael Jackson"
# we could do 
print(name[0:5])
#which meant start from index 0 and end before index 5


#Deleting a range using del is also quite the same 
#say:
numbers = ["A","B","C","D","E","F","G","H"]
del numbers[0:5]
print(numbers)