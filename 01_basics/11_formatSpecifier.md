# 📖 Python Format Specifiers

Format specifiers in Python are placeholders used inside strings to dynamically insert values and control their formatting. They're widely used with the `format()` method, **f-strings**, and even the older `%` operator.

---

## 📌 Why Use Format Specifiers?
- To **control alignment, width, precision, and representation** of printed values.
- To format numbers, strings, or other data types in a structured and visually clear way.
- To improve the readability of console outputs, logs, and reports.

---

## 📚 Types of Format Specifiers

| Symbol | Meaning                          | Example Output |
|:--------|:--------------------------------|:----------------|
| `d`      | Integer                          | `10`             |
| `f`      | Floating-point number            | `3.14`          |
| `.2f`    | Floating-point (2 decimal places)| `3.14`          |
| `s`      | String                            | `Hello`         |
| `%`      | Percentage (for f-strings/format)| `75.00%`        |
| `x` / `X`| Hexadecimal (lower/upper)        | `1a` / `1A`     |
| `o`      | Octal                            | `12`            |
| `b`      | Binary                           | `1010`          |

---

## ✳️ Syntax

**Using `format()` method**
```python
"Hello, {}!".format("World")
```
**Output**
```
Hello, World!
```

**Using f-strings (Python 3.6+)**
```python
name = "World"
print(f"Hello, {name}!")
```
**Output**
```
Hello, World!
```

**Using old `%` formatting**
```python
name = "World"
print("Hello, %s!" % name)
```
**Output**
```
Hello, World!
```

---

## 📌 Code Examples with Output

### 🔸 Integer Formatting
```python
num = 25
print("Number: {}".format(num))
print(f"Number: {num}")
print("Number: %d" % num)
```
**Output**
```
Number: 25
Number: 25
Number: 25
```

---

### 🔸 Floating-Point with Precision
```python
pi = 3.14159
print("Value of pi: {:.2f}".format(pi))
print(f"Value of pi: {pi:.3f}")
```
**Output**
```
Value of pi: 3.14
Value of pi: 3.142
```

---

### 🔸 String Alignment and Width
```python
text = "Python"
print("{:<10}".format(text))  # Left align
print("{:>10}".format(text))  # Right align
print("{:^10}".format(text))  # Center align
```
**Output**
```
Python    
    Python
  Python  
```

---

### 🔸 Number Base Conversion
```python
num = 255
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hex (lower): {num:x}")
print(f"Hex (upper): {num:X}")
```
**Output**
```
Binary: 11111111
Octal: 377
Hex (lower): ff
Hex (upper): FF
```

---

### 🔸 Percentage Formatting
```python
progress = 0.756
print(f"Completion: {progress:.2%}")
```
**Output**
```
Completion: 75.60%
```

---

### 🔸 Combining Different Specifiers
```python
name = "Alice"
score = 92.3456
print(f"{name:^10} | Score: {score:>7.2f}%")
```
**Output**
```
  Alice    | Score:   92.35%
```

---

## 📌 Best Practices
- ✅ Prefer **f-strings** for cleaner, faster, and more readable code (Python 3.6+).
- ✅ Use format specifiers to enhance the clarity of numeric or string outputs.
- ⚠️ Avoid the old `%` formatting style in new projects — retained mostly for legacy code.

---

## 📖 References
- [Official Python Docs — str.format()](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [PEP 498 — Literal String Interpolation (f-strings)](https://peps.python.org/pep-0498/)

---

## 📌 Conclusion
Format specifiers are a powerful way to control how values are displayed in Python, making your outputs more structured and professional. Mastering them helps you produce clean and well-formatted code.
