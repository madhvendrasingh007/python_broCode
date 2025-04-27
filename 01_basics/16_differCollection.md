# Python Collections Comparison: Lists, Tuples and Sets

This guide demonstrates the key differences between Python's three main collection types through practical code examples.

## Creating Collections

```python
# Different syntax for creation
my_list = [1, 2, 3, 2, 3]
my_tuple = (1, 2, 3, 2, 3)
my_set = {1, 2, 3, 2, 3}

print(my_list)   # [1, 2, 3, 2, 3] - keeps duplicates, preserves order
print(my_tuple)  # (1, 2, 3, 2, 3) - keeps duplicates, preserves order
print(my_set)    # {1, 2, 3} - removes duplicates, no guaranteed order
```

## Mutability: Modifying Collections

```python
# Lists are mutable
fruits_list = ["apple", "banana", "cherry"]
fruits_list[0] = "orange"  # Changing element
fruits_list.append("kiwi") # Adding element
print(fruits_list)  # ['orange', 'banana', 'cherry', 'kiwi']

# Tuples are immutable
fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple[0] = "orange"  # ERROR: TypeError: 'tuple' object does not support item assignment
# fruits_tuple.append("kiwi")  # ERROR: 'tuple' object has no attribute 'append'

# Sets are mutable but unindexed
fruits_set = {"apple", "banana", "cherry"}
# fruits_set[0] = "orange"  # ERROR: 'set' object does not support indexing
fruits_set.add("kiwi")  # Adding element
fruits_set.remove("apple")  # Removing element
print(fruits_set)  # {'cherry', 'banana', 'kiwi'} - order not guaranteed
```

## Accessing Elements

```python
colors_list = ["red", "green", "blue", "yellow"]
colors_tuple = ("red", "green", "blue", "yellow")
colors_set = {"red", "green", "blue", "yellow"}

# Lists and tuples support indexing
print(colors_list[0])   # red
print(colors_tuple[0])  # red
print(colors_list[-1])  # yellow
print(colors_tuple[-1]) # yellow

# Sets don't support indexing
# print(colors_set[0])  # ERROR: 'set' object is not subscriptable

# Lists and tuples support slicing
print(colors_list[1:3])  # ['green', 'blue']
print(colors_tuple[1:3]) # ('green', 'blue')

# Sets don't support slicing
# print(colors_set[1:3])  # ERROR: 'set' object is not subscriptable
```

## Performance Differences

```python
import time

# Speed test for membership testing (in operator)
large_list = list(range(10000))
large_tuple = tuple(range(10000))
large_set = set(range(10000))

# Test list search
start = time.time()
9999 in large_list  # Searches sequentially (slower)
print(f"List search time: {time.time() - start}")

# Test tuple search
start = time.time()
9999 in large_tuple  # Also searches sequentially (slower)
print(f"Tuple search time: {time.time() - start}")

# Test set search
start = time.time()
9999 in large_set  # Uses hash table (much faster)
print(f"Set search time: {time.time() - start}")

# Output (times will vary):
# List search time: 0.00096...
# Tuple search time: 0.00091...
# Set search time: 0.00001... (significantly faster)
```

## Use Cases and Unique Operations

```python
# 1. Lists: When order matters and items will change
tasks = ["Code", "Test", "Debug"]
tasks.append("Deploy")
tasks.sort()
print(tasks)  # ['Code', 'Debug', 'Deploy', 'Test']

# 2. Tuples: For fixed collections and multiple return values
def get_coordinates():
    return (10.5, 25.3)  # Return multiple values as tuple

lat, long = get_coordinates()  # Tuple unpacking
print(f"Latitude: {lat}, Longitude: {long}")

# 3. Sets: For membership testing and mathematical operations
users_set_a = {"Alice", "Bob", "Charlie"}
users_set_b = {"Charlie", "Dave", "Eve"}

# Find users in both sets
print(users_set_a & users_set_b)  # {'Charlie'} - Intersection

# Find all unique users
print(users_set_a | users_set_b)  # {'Bob', 'Alice', 'Charlie', 'Dave', 'Eve'} - Union

# Find users in A but not in B
print(users_set_a - users_set_b)  # {'Bob', 'Alice'} - Difference
```

## Memory Usage

```python
import sys

# Create identical data in different collection types
data_list = [1, 2, 3, 4, 5]
data_tuple = (1, 2, 3, 4, 5)
data_set = {1, 2, 3, 4, 5}

# Check memory size (in bytes)
print(f"List size: {sys.getsizeof(data_list)} bytes")
print(f"Tuple size: {sys.getsizeof(data_tuple)} bytes")
print(f"Set size: {sys.getsizeof(data_set)} bytes")

# Tuples typically use less memory than lists
# Sets use more memory due to hash table structure
```

## Summary of Differences

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Mutability | Mutable | Immutable | Mutable |
| Duplicates | Allowed | Allowed | Not allowed |
| Order | Preserved | Preserved | Not preserved |
| Indexing | Yes | Yes | No |
| Use Cases | General-purpose, items need to change | Data protection, hashable (can be dictionary keys) | Removing duplicates, membership testing, mathematical set operations |