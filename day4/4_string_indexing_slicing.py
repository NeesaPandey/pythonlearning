# String indexing and slicing is similar to that of list
# Forward indexing starts from 0 and reversing indexing starts from -1

# string indexing
message = "Hello World"
print(message[5])   # "Hello"
print(message[0:5])  # "Hello
print(message[3:])  # "lo World"
print(message[-4:-2])  # "or"
#print(message[20])  # error


# string slicing
message = "Hello World"
print(message[0])  # H
print(message[3])  # l
print(message[-1])  # d
print(message[:5])   # Hello
#print(message[20])  # error

# Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")  # Yes, 'free' is present.

message = "Hello World"
# message[2] = "L"  raise error as string is immutable
del message  # it deletes the strings

# Iterating the string
message = "Hello World"
for each in message:
    print(each)  # "H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"

message = "Hello World"
for each in message[:5]:
    print(each)  # "H", "e", "l", "l", "o", " "
