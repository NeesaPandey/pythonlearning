#VARIABLES

x = 5
y = "John"
print(x)
print(y)

#Casting: If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#2myvar = "John"  incorrect
#my-var = "John"  incorrect
#my var = "John"  incorrect

#Global variable: Variables that are created outside of a function

x = "awesome"
def myfunc():
    print("Python is " + x)  # Python is awesome
myfunc()

#when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


