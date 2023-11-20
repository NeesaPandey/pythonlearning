# operators
# operator are the symbols in python or in programming language that carry out arithmetic and logical operations
# pythons operators are
# 1. Arithmetic
# 2. Relational
# 3. Logical
# 4. Membership
# 5. Identity
# 6. Assignment

# arithmetic

# addition,subtraction,multiply,division
a = 14
b = 20

# modulus:remainder
print(a % b)

# exponential(**)
print(a ** 2)  # 5**2
print(a ** 3)  # 4**3

# floor division(//)
# omits the decimal value from the division operation and gives floor values(small value )

#####Comparision operator ###
# =,<,>,>=,<=,!=

# logical
# and,or,not
print(a > b or b != a)
print(a > b or a != b)
# print(not true) # false
# print(not false) # true

a = 5
print(not a)  # false [non zero and not null are true]
a = 0
print(not 0)  # true

# Assignment operator
# is equals to (=)
c = 2 + 3
# here 2 and 3 are added and assigned to a variable 'a' using assignment operator
print(c)

a = 1
a = a + 1
print(a)  # 2
a += 1  # 3
# here += is also assignment operator
# similarly -=,/=,*=,
a = 20
a %= 2
print(a)  # gives 0

# membership operators
# in and not in are the membership operators.we can use membership operators in sequence datatypes
print(2 in [1, 2, 3])  # true
print(3 not in [1, 2, 3])  # false

# identity operators
# "is" and "is not"
a = [1, 2, 3]
b = a
print(a is b)  # true
# here a and b are the same object and lies in same memory location
print(id(a) == id(b))

b = a.copy()
print(a is b)  # false
print(id(a) == id(b))  # false
# here a and b have same value but are in different memory location


###Precedence and Associativity
# if an operation has multiple operators then precedence defines the order of such operators
# if multiple operators have same precedence then the operator is done based on associativity
# normally it is left to right but if exponential(**) exist then right to left

print(2 * 3 / 3)  # 2
print(2 ** 3 ** 2)  # 512
