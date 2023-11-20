#String are the immutable datatypes in Python
#they are sequential datatypes (iterables)

# Creating an empty string
a = ""
b = ''
c = """ """  # docstring / triple quoted string
d = ''' '''  # docstring / triple quoted string
e = str()    # str() is a builtin op

#Quote characters
message = " I'm learning Python "  # double quote outside and single quote inside
#message = ' I'm learning Python ' # wrong
print(message)

#But we have the feature of escape sequence in Python if we want to use single quote both inside and outside

message = ' I\'m learning Python '  # here \' is an escape sequence

#escape sequence suppress the usual meaning of character and gives new meaning
# \' , \" , \n , \t etc are escape sequence

######### Triple Quoted Strings ####

#Triple quoted strings cab be used as docstring. We can write docs for function and classes using
#triple quoted strings. sometimes they are also used as multi-lined comments
#they can be stored in variable like regular strings

def addition(a,b):
    """
    This is a function to add two integers
    :param a: First integer input
    :param b: Second integer input
    :return: sum of a and b
    """
print(help(addition))