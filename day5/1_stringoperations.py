#Concatenation : We can concatenate strings using "+" operator

m1 = "Hello"
m2 = "World"
print(m1+m2)  # HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)          # Hello World

# Repetition/Broadcast operation : Broadcast in string is done using * operator
message = "Hello"
print(message * 3)  # HelloHelloHello

# Membership operation
print("m" in "message")  # true
print("e" not in "message")  # false

# Built-in function
# 1. len() : gives length of sequential datatypes ( list, string, tuples, etc)
message = "Hello World"
print(len(message))  # 11

# 2. type() : return the type of any object
print(type(message))  # <class "str">

# 3. slice() : this function is similar to string and list slicing

sliced_data = slice(2,7)
print(message[sliced_data])  # llo World


