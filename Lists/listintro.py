#Okay ,lets start with the generics before lists were introduced.

#how fun is this ? 

name1 = "Ngawang"
name2 = "moon"
name3 = "Rockefeller"
name4 = "Elon Musk"
name5 = "Jesus"
#and so on .....
#it seems completely harmless.. but just imagine a database where you have to maybe
#insert 10000 of names, data like this .. and imagine the amount of storage required for this.

#so we use lists.

#with lists we can do directly :

name = ["Michael","Jonathan","James"]
#In this here name stores 3 different str's.
print(name)

#Lists also allows us to store different data types.
naru = ["Mihael" , 30 , True, 3.5]

#What we must also understand is this that:
#Lists are ordered by nature.
#So every element in the list can be / must be accessed through an index.
#.i.e. 
print(naru[0]) #This prints Mihael
print(naru[1]) #This prints 30.

#As , we start from Index 0 --> soon.
#We can also use negative indexing.

#for example: we have 3.5 as -1 , TRUE = -2 , 30 = -3 , Mihael = -4.....
