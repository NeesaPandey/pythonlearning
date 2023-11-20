#we can loop (for loop) through the list in following ways

a = [1, 2, 3, 4]
for i in a:
    print(i)

b=a.copy()
for i in b:
    print(i**2)

#OR

b=list()
for i in a:
    value = i**2
    b.append(value)
print(b)
print(a)


b=[i**2 for i in a] # list comprehension
print(b)

#without comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)  # ['apple', 'banana', 'mango']

# with

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # ['apple', 'banana', 'mango']

# syntax  :  newlist = [expression for item in iterable if condition == True]

# iterable

a = [ x for x in range(5)]
print(a)  # [0, 1, 2, 3, 4]

a = [ x for x in range(15) if x > 3]      # condition
print(a) # [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]



