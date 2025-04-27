# Python Operators Guide

A comprehensive guide to Python's operators with examples.

## 1. Arithmetic Operators

Used for mathematical calculations:

```python
a, b = 10, 3

# Basic operations
print(a + b)   # 13 (Addition)
print(a - b)   # 7 (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.3333... (Division)
print(a % b)   # 1 (Modulus - remainder)
print(a ** b)  # 1000 (Exponentiation - 10^3)
print(a // b)  # 3 (Floor division - integer division)
```

## 2. Assignment Operators

Used to assign values to variables:

```python
x = 10
x += 5   # Same as: x = x + 5 (x becomes 15)
x -= 3   # Same as: x = x - 3 (x becomes 12)
x *= 2   # Same as: x = x * 2 (x becomes 24)

# Walrus operator (:=) - assign and return value
print(y := 20)  # Assigns 20 to y and prints 20
```

## 3. Comparison Operators

Used to compare values:

```python
a, b = 5, 10
print(a == b)  # False (Equal)
print(a != b)  # True (Not equal)
print(a > b)   # False (Greater than)
print(a < b)   # True (Less than)
print(a >= b)  # False (Greater than or equal)
print(a <= b)  # True (Less than or equal)
```

## 4. Logical Operators

Used to combine conditional statements:

```python
x = 5
print(x > 3 and x < 10)  # True (both conditions are true)
print(x > 3 or x > 10)   # True (at least one condition is true)
print(not(x > 3))        # False (reverse the result)
```

## 5. Identity Operators

Compare if objects are the same (same memory location):

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True (x and z reference the same object)
print(x is y)      # False (different objects)
print(x is not y)  # True (not the same object)
```

## 6. Membership Operators

Test if a value exists in a sequence:

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("pineapple" not in fruits)  # True
```

## 7. Bitwise Operators

Manipulate binary representations:

```python
a, b = 10, 4  # In binary: a = 1010, b = 0100
print(a & b)  # 0 (AND: 0000)
print(a | b)  # 14 (OR: 1110)
print(a ^ b)  # 14 (XOR: 1110)
print(~a)     # -11 (NOT)
print(a << 2) # 40 (Shift left by 2: 101000)
print(a >> 2) # 2 (Shift right by 2: 10)
```

## Operator Precedence

Operations are performed in this order:

1. `()` - Parentheses
2. `**` - Exponentiation
3. `+x`, `-x`, `~x` - Unary operators
4. `*`, `/`, `//`, `%` - Multiplication, division
5. `+`, `-` - Addition, subtraction
6. `<<`, `>>` - Bitwise shifts
7. `&` - Bitwise AND
8. `^` - Bitwise XOR
9. `|` - Bitwise OR
10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` - Comparisons
11. `not` - Logical NOT
12. `and` - Logical AND
13. `or` - Logical OR

```python
# Example of precedence
result = 10 + 3 * 2  # 16 (not 26)
print(result)

# Using parentheses to change precedence
result = (10 + 3) * 2  # 26
print(result)
```