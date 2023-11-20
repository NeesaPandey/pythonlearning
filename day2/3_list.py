 #python list are mutable data-types and are sequential(iterable)
#list are created enclosing data in big bracket[] or using built-in function list()

#creating an empty list
a=[]
b=list()

#non-empty
a=[1,2,3]
vowels=["a","e","i","o","u"]

#if same datatype list are homogeneous else heterogenous
a=[1,2.3,["a","b"]]

##### ACCESSING LIST ITEMS #####
#List items can be accessed using indexing and slicing

#INDEXING in list starts from 0 for forward traverse and -1 for reserve traverse
vowels=["a","e","i","o","u"]
print(vowels[0])       #a
print(vowels[-1])      #u
print(vowels[10])      #index error

#index must be integer

##### LIST SLICING #####
a=["a","b","c","d","e","f","g","h","i","j"]
print(a[0:5]) #["a",b","c","d","e"]
print(a[:5]) #["a",b","c","d","e"]
print(a[2:]) #["c","d","e","f","g","h","i","j"]
print(a[0:-2]) #["a","b","c","d","e","f","g","h"]
print(a[-2:0]) #[]


##### LIST OPERATION #####

 #concatenation
 a=[1,2,3]
 b=[4,5,6]
 result=a+b
 print(result)  #[1,2,3,4,5,6]

 #membership
 print(2 in [1,2,3]) # true
 print(3 not in [1,2,3]) # false