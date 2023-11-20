#append()
vowels = ["a", "e", "i", "o"]
vowels.append("u")
print(vowels)

#extend
a=[1, 2, 3]
b=[4, 5, 6]
result=a.extend(b)
print(result) #none
print(a) #[1,2,3,4,5,6]

#insert(index,value)
vowels=["a", "e", "o", "u"]
vowels.insert(2,"i")
print(vowels)

#remove(value)
a=[1,2,3,4,5]
a.remove(3)
print(a)
#a.remove(6) #error

#replacing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

#pop(index) : pop keyword also removes the specified inde
vowels=["a", "e", "i", "o", "u"]
result=vowels.pop(1)
print(result) #e
print(vowels) #[a,i,o,u]

#pop() methods doesnt necessarily take a parameter.if parameter not provided then last ites  from the list is popped out

#del(index)  :del keyword  removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist

#clear()
a=[1,2,3,4]
a.clear()
print(a)  # []

#index(value,start,end)
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("i")
print(result)

a= [1,2,3,4,5,6,7,3,4,2,5,6]
result=a.index(2,2)
print(result)  #9

result= a.index(2,2,10)
print(result)

#count()
a=[1,2,3,4,1,1,2,3,1]
print(a.count(1))  #4
print(a.count(4))  #1

#reverse()
a=[2,1,10,9,3]
a.reverse()
print(a) #[3,9,10,1,2}




