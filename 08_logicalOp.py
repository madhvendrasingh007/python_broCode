#Logical Operators
#Logical operators are used to combine conditional statements.

#In Python, there are three logical operators:
#and -> Returns True if both statements are true
#or -> Returns True if one of the statements is true
#not -> Returns True if the statement is false

#Example of "and" logical operator
a = 10
b = 20
c = 30
if a < b and b < c:
    print("Both conditions are True")
else:   
    print("One or both conditions are False")

#Example of "or" logical operator
a = 10
b = 20
c = 30
if a < b or b > c:
    print("At least one condition is True")
else:
    print("Both conditions are False")

#Example of "not" logical operator
a = 10
b = 20
if not a > b:
    print("a is not greater than b")   
else:
    print("a is greater than b")