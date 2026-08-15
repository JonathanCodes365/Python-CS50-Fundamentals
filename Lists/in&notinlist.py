#As similar to how we used "in" in string.

#we can use "in " in lists as well.
#the syntax is essentially the same

#in gives us the result true or false

numbers = [10,20,30,40,50]
print(30 in numbers)

#now what if the question is to find whether there is a number 30 and 99 in the list or not .

#so for that we can use in or not in the list to find out whether a particular number is in the list or not.

#our usual approach might be to use something like 

# if number[0] ==30 , number[1]==30 , number[2]==30.....:
# print ...
#i am not saying you cant do this or this is incorrect but it is mundane and dull to keep on writing for
#tens and thousand of data entry.

#to do this we simply do :
if 30 in numbers:
    print("30 is in the list")#We essentially said if in returns true...
    #It is in the list

#we can also do 
if 99 in numbers:
    print("99 is in the list")
else:
    print("99 is not in the list")

#we can also use "not in "
#example:

if 99 not in numbers:
    print("99 is not in the list")
else:
    print("99 is in the list")