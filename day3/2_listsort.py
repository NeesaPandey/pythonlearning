# sort(reserve=true, key=function) method

a=[5, 3, 10, 1, 12, 2, 6]
a.sort()
print(a)  # [1, 2, 3, 5, 6, 10, 12]

a.sort(reverse=True)
print(a)  # [12,10,6,5,3,2,1]

a.reverse()
print(a)  # [12,10,6,5,3,2,1]

a=[(5,4),(3,2), (4,10), (12,11), (1,9)]
#output = [(3,2),(5,4), (1,9),(4,10), (12,11)]

a=[[1, 4], [2, 3], [0, 5]]

def get_second_num(data):
    return data[1]


a.sort(key=get_second_num)
print(a)

a=[(4,12,5), (6,1), (11,12), (6,7,8)]
def get_sort(data):
    return data[-1]
a.sort(key=get_sort) #[(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]
a.sort(key=get_sort,reverse=True) #[(11, 12), (6, 7, 8), (4, 12, 5), (6, 1)]
print(a)

a = ["orange", "mango", "kiwi", "pineapple", "banana"]
newlist = sorted(a)
print(newlist)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
# Use sorted() to create a new sorted list
#sorted_list = sorted(original_list)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

def sortf(n):
   return abs(n-20)  # absolute subtract
list = [1, 5, 30, 25]
list.sort(key=sortf)
print(list)  # [25, 30, 5, 1]

