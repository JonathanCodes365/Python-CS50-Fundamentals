#We are doing this after we did the remove from a list...

#Pop as we have previously studied as well is a stack operation ...

#So essentially pop and remove does the same function in a list.
#it removes a element from a list.

#but unlike remove --> which just removes an element from the text.
# pop --> is more like remove an element + store it.

numbers = [10,20,30,40,50]
numbers.remove(10)
print(numbers)
#the o/p is [20, 30, 40, 50] ... the 10 is just removed

#but if we want to remove 20 and we do pop...Unlike remove which directlyy uses the elemnt.
#in pop we use the index of the list.
x = numbers.pop(0) 
print(x)
#we get to store the removed value in a different variable
