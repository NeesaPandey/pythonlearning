#Note: All string methods return new values. They do not change the original string.

# 1. capitalize()
message = "hello world"
result = message.capitalize()
print(result)  # Hello world

# 2. title()
result = message.title()
print(result)  # Hello World

# 3. upper()
result = message.upper()
print(result)  # HELLO WORLD

# 4. lower()
result = message.title()
print(result)  # hello world

# 5. strip() : removes whitespaces at start and end
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# split()
message = "hello world . I am learning python"
result = message.split()  # calling split() without any parameters. It splits with <space> by default
print(result)  # ['hello', 'world', '.', 'I', 'am', 'learning', 'python']

result = message.split("o")
print(result)  # ['hell', ' w', 'rld.I am learning pyth', 'n']  {separate by o and del o}

message = "hello,all,i,am,learning,python"
result = message.split(",")
print(result)  # ['hello', 'all', 'i', 'am', 'learning', 'python']

# join()
info = ['hello', 'all', 'I', 'am', 'learning', 'python']
result = " ".join(info)
print(result)  # hello all I am learning python

result = "+".join(info)
print(result)  # hello+all+I+am+learning+python

result = ",".join(info)
print(result)  # hello,all,I,am,learning,python

# info.join(" ")  [error because join() should be called with string object not with list

# find()
message = "hello message"
result = message.find('m')
print(result)  # 6

result = message.find('age')
print(result)  # 10  #index of "a"

result = message.find('w')
print(result)  # -1  error(is string not found)

search_value = "Age"
result = message.lower().find(search_value.lower())
print(result)  # 10

# So if you want a case-insensitive sort function, use str.lower as a key function:
# thislist.sort(key = str.lower)

# replace()
message = "hello world"
result = message.replace("hello", "Hello")
print(result)  # Hello world

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)  # ['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']


