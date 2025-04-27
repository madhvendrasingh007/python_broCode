# Python Strings

A guide to strings in Python and their most useful methods.

## String Characteristics
- Sequence of characters
- Immutable (cannot be changed after creation)
- Ordered
- Iterable

## Basic String Operations

```python
name = "John Doe"

# Get string length
print(len(name))  # 8

# Searching methods
name.find("o")       # 1 - Index of first occurrence
name.find("o", 5)    # 6 - Search from index 5
name.find("o", 0, 5) # 1 - Search between index 0 and 5
name.rfind("o")      # 6 - Index of last occurrence

# Case manipulation
name.capitalize()    # "John doe" - First character uppercase
name.upper()         # "JOHN DOE" - All uppercase
name.lower()         # "john doe" - All lowercase

# Character checks
name.isdigit()       # False - Is the string all digits?
name.isalpha()       # False - Is the string all alphabetic? (False because of space)
name.isalnum()       # False - Is the string all alphanumeric? (False because of space)

# Replacement
phone = "1234567190"
phone.isdigit()           # True
phone.replace("1", "9")   # "9234567990" - Replace all occurrences
phone.replace("1", "9", 1) # "9234567190" - Replace first occurrence only
phone.replace("1", "9", 2) # "9234567990" - Replace first two occurrences
```

## Additional String Methods

```python
# Splitting and joining
sentence = "Hello, how are you?"
words = sentence.split() # ["Hello,", "how", "are", "you?"]
comma_split = sentence.split(",") # ["Hello", " how are you?"]
"-".join(words) # "Hello,-how-are-you?"

# Stripping whitespace
text = "   Python is amazing!   "
text.strip()    # "Python is amazing!" - Remove whitespace from both ends
text.lstrip()   # "Python is amazing!   " - Remove leading whitespace
text.rstrip()   # "   Python is amazing!" - Remove trailing whitespace

# Checking string properties
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True
"123".zfill(5)            # "00123" - Pad with zeros to width 5

# Format and align
name = "John"
"Hello, {:10}!".format(name)  # "Hello, John      !" - Right-aligned in 10 spaces
"Hello, {:<10}!".format(name) # "Hello, John      !" - Left-aligned in 10 spaces
"Hello, {:^10}!".format(name) # "Hello,    John   !" - Center-aligned in 10 spaces

# Count occurrences
"banana".count("a")  # 3 - Count occurrences of "a"

# Partition
"key=value".partition("=")  # ("key", "=", "value")

# Check if all characters meet a condition
"123".isnumeric()  # True
"HELLO".isupper()  # True
"hello".islower()  # True
"Title Case".istitle()  # True - Each word starts with uppercase
```

## String Slicing

```python
text = "Python Programming"
text[0]     # "P" - First character
text[-1]    # "g" - Last character
text[0:6]   # "Python" - Characters from index 0 to 5
text[7:]    # "Programming" - Characters from index 7 to end
text[:6]    # "Python" - Characters from start to index 5
text[::2]   # "Pto rgamn" - Every second character
text[::-1]  # "gnimmargorP nohtyP" - Reverse string
```