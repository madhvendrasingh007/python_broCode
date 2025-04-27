# Python Type Casting

A concise guide to converting between Python data types.

## Implicit Type Conversion

Python automatically converts some types in specific contexts:

```python
x = 10    # int
y = 3.14  # float
z = x + y # Python implicitly converts x to float
print(z)  # 13.14 (float)
```

## Explicit Type Conversion

### Integer Conversion
```python
# String to int
age_str = "25"
age_int = int(age_str)  # 25 (int)

# Float to int (truncates decimal part)
height = 5.9
height_int = int(height)  # 5 (int)

# Boolean to int
is_active = True
active_int = int(is_active)  # 1 (int)
```

### Float Conversion
```python
# String to float
price_str = "19.99"
price = float(price_str)  # 19.99 (float)

# Integer to float
count = 10
count_float = float(count)  # 10.0 (float)
```

### String Conversion
```python
# Int to string
qty = 42
qty_str = str(qty)  # "42" (str)

# Float to string
pi = 3.14159
pi_str = str(pi)  # "3.14159" (str)

# Boolean to string
is_member = True
member_str = str(is_member)  # "True" (str)
```

### Boolean Conversion
```python
# Numeric to boolean (0 is False, any other number is True)
zero = bool(0)    # False
one = bool(1)     # True
neg = bool(-3.14) # True

# String to boolean (empty string is False, any other string is True)
empty = bool("")  # False
text = bool("hi") # True
```

## Type Checking
```python
value = "123"
print(type(value))        # <class 'str'>
value = int(value)
print(type(value))        # <class 'int'>
```

## Error Handling

Handle conversion errors with try/except:
```python
try:
    number = int("hello")  # Will raise ValueError
except ValueError:
    print("Conversion failed")  # Conversion failed
```