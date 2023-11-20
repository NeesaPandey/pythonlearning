# We do string formatting using f-string

programming_language = input("Enter a language")
message = f"I am learning {programming_language}"
print(message)  # Enter a language: python
# I am learning python

name = "john doe"
age = 23
message = f"hello i am {name} .I am {age} years old"
print(message)

price = 49.09912
txt =f"For only {price:.2f} dollars!"  # only up to 2 float data
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)  # I want 3 pieces of item 567 for 49.95 dollars.








