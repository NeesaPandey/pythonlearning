#Create a list of first 10 multiples of 3 using list comprehension
range(7)
print(list(range(7)))  # [0, 1 ,2 ,3 ,4, 5, 6]


a=range(1,11)
for i in a:
    print(3*i)

a=[]
for value in range(1, 11): #1,2,....
    a.append(value *3) #[3,6,9,...30]
print(a)

#using comprehension
a=[i * 3 for i in range(1,11)]
print(a)
