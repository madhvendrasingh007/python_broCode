# Python Input Function

A guide to using the `input()` function and handling type conversion for user input.

## Basic Input Usage

The `input()` function captures user input from the console as a string:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
```

## Type Conversion is Required

Input data is always returned as a string, regardless of what the user types.

### Common Error

```python
age = age + 1  # ERROR: This fails because you can't add 1 to a string
```

This causes a `TypeError` because Python cannot add an integer to a string.

### Correct Approaches

Method 1: Convert after input
```python
age = input("Enter your age: ")
age = int(age) + 1  # Convert string to integer, then add 1
print(f"Hello {name}, you are {age} years old.")
```

Method 2: Convert during input capture
```python
age = int(input("Enter your age: ")) + 1
print(f"Hello {name}, you are {age} years old.")
```

## Best Practices

- Always convert input to the appropriate data type before performing operations
- Use `int()` for whole numbers, `float()` for decimal numbers
- Consider using error handling (try/except) to prevent crashes from invalid input
- Use string formatting (f-strings) to display results with variables

## Example Output

If user enters "John" and "25":
```
Hello John, you are 26 years old.
```