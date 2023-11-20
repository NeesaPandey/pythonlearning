a= [1, 2, 3,4]
b= a
print(a) # [1, 2, 3,4]
print(b) # [1, 2, 3,4]
print(a is b) #true


b=a.copy()
print(a) # [1, 2, 3,4]
print(b) # [1, 2, 3,4]
print(a is b) #false

#shallow copy
a=[[1,2,3],4, 5]
b=a.copy()
a[0][1]=7
print(a) #[[1,7,3],4, 5]
print(b) #[[1,7,3],4, 5]

#even if 'b' is copy of 'a' , if we change any mutuable obj inside 'a'then
#the change is also reflected in 'b'. this type of copy is called shallow copy

##### Deepcopy
from copy import deepcopy

a=[[1,2,3],4, 5]
b=deepcopy(a)
print(a) #[[1,2,3],4, 5]
print(b) #[[1,2,3],4, 5]

a[0][1]=7
print(a) #[[1,7,3],4, 5]
print(b) #[[1,7,3],4, 5]









