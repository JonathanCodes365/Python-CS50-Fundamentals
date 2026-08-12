#We are doing this after doing the extend method 
#and before we did the extend we did the append method.

#What we learnt from both of them broadly speaking was to add them in our list.

name = [1,2,3,4]
name.append(5)
print(name) #[1, 2, 3, 4, 5 : we got this as our result

name.extend([6,7])
print(name) #[1, 2, 3, 4, 5, 6, 7] :we got this as our result.

#Notice how append starts from the right hand.
#and list 6.7 adds up wherever it is located...
#so , there is not much choice on where to add when using extend  and append.

#5 as added after 4.
#6 and 7 were added after 5.

#what if i want to insert from the middle or the beginning?

#Yes, we use insert method for that very purpose

#example:

rati = [1,2,3,4,5]
rati.insert(0,0.5)
#It simply says go at index 0 and insert 0.5
print(rati)


#So, we use append for inserting at the end
#Insert to insert at a location "we want".
#Well, extend is extend just vibing and adding up at it's designated area.