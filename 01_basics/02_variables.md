# Python Variables and String Formatting

A demonstration of Python data types and string manipulation techniques.

## Variables and Data Types

```python
first_name = "Kevin"       # String - text data
last_name = "Robinson"     # String - text data
age = 30                   # Integer - whole number
height = 5.9               # Float - decimal number
is_student = True          # Boolean - True/False value
```

The script shows how to check variable types using `type()`:
```python
print(type(first_name))    # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height))        # <class 'float'>
print(type(is_student))    # <class 'bool'>
```

## String Formatting Methods

### F-strings
Clean, readable way to embed variables in strings:
```python
print(f"Hello, my name is {first_name} {last_name} and I am {age} years old.")
# Output: Hello, my name is Kevin Robinson and I am 30 years old.
```

### String Concatenation
Joining strings with the `+` operator:
```python
print("first_name" + first_name)  # Output: first_nameKevin
```

Note: Cannot concatenate strings with other types directly:
```python
# This causes error: print("age" + age)
print("age" + str(age))    # Works after conversion: age30
```

### Other Formatting Methods
```python
print(f"age {age}")        # F-string: age 30
print("age {}".format(age))  # format() method: age 30
print("age %d" % age)      # % operator: age 30
```

## Usage
Run the script to see all variable types and formatting outputs.