# true and false are the boolean datatypes in python .
# keywords "True" and "False" are used to represent true and false state respectively

###Operations that give boolean types ###
#1 . Comparision operation
a = 5
b = 3
print(a < b)  # False
print(a > b)  # True
print(a >= b)  # True
print(a <= b)  # False
print(a != b)  # True
print(a == b)  # False

# Logical
a = 5
b = 3
print(a >b and b != a) # True
print(a != b or a > b ) # True
print(not True) # False
print(not False) # True

#Membership Operation
print("a" in ["a", "e", "i"])  # True

#Identity Op
a = 1
b = 1
print(a is b)  # True
print(id(a) == id(b)) # True
print(a is not b) # False
print(id(a) != id(b)) # False

#Concept of truthy and falsy

a= 5
print(not a) #False

#Any non-zero or non-empty datatype including True itself is a truthy datatype
# 5,1,-23, [1,2] {-4,-4,"a"},{"a":1},True ; all these data are truthy data types

#In contrast, all empty datatypes, zero and None including False are falsy datatypes

#How can we verify data is Truthy and Falsy?
#We can use bool() built in function

#check for truthy
a= 4
b= -3
c= [1,2,3]
d=(1,2)
e= {1,2}
f={"a":1}
g="Hello World"
h = True
print(bool(a))  # True
print(bool(b))  # True
print(bool(c))  # True
print(bool(d))  # True
print(bool(e))  # True
print(bool(f))  # True
print(bool(g))  # True
print(bool(h))  # True

#Applying not operation to any truthy value results in False
print(not a)  # False

# Check for falsy
a=0
b = []
c = {}
d = ()
e = set()
f = ''
g = None
h = False
print(bool(a))  # False
print(bool(b))  # False
print(bool(c))  # False
print(bool(d))  # False
print(bool(e))  # False
print(bool(f))  # False
print(bool(g))  # False
print(bool(h))  # False
print(bool())  # False

#Applying not operation to any falsy value result in True
print(not a)  # true
print(not None)  # true

###Python Boolean is a Sub-class of Integer
#True is integer 1 and False is integer 0

print(True + 1)  #2
print(70 * False)  #0
print(True + True) #2
print(True +  False) #1

