#conditional expressions
# A conditional expression is an expression that evaluates to one of two values based on a condition.
# It is often used as a shorthand for an if-else statement.
# The syntax for a conditional expression is:
# value_if_true if condition else value_if_false

num = 10
print("Positive" if num>0 else "Negative")  # Output: Positive
# The conditional expression can also be used to assign a value to a variable based on a condition.
result = "Positive" if num > 0 else "Negative"
print(result)  # Output: Positive

# You can also use conditional expressions in more complex expressions.
def get_sign(num):
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(get_sign(10))  # Output: Positive