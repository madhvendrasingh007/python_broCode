# Python Collections: Lists, Tuples, and Sets

A comprehensive guide to the three main sequence collection types in Python.

## Collection Types Overview

Python offers several built-in collection types:
- **Lists** `[]` - ordered, mutable, allows duplicates
- **Tuples** `()` - ordered, immutable, allows duplicates
- **Sets** `{}` - unordered, mutable, no duplicates
- **Dictionaries** `{}` - unordered, mutable, key-value pairs

## 1. Lists

### List Basics

```python
# Creating a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # ['apple', 'banana', 'cherry']
print(type(fruits))  # <class 'list'>

# Accessing elements
print(fruits[0])  # 'apple' - first element
print(fruits[-1])  # 'cherry' - last element

# Slicing
print(fruits[1:3])  # ['banana', 'cherry'] - elements from index 1 to 2
print(fruits[::-1])  # ['cherry', 'banana', 'apple'] - reverse order

# Iterating through a list
for f in fruits:
    print(f)  # prints each element on a new line

# Checking membership
print('banana' in fruits)  # True - checks if 'banana' is in the list
```

### List Methods

```python
# Adding elements
fruits.append('orange')  # Adds to the end
fruits.insert(1, 'kiwi')  # Inserts at index 1
fruits.extend(['mango', 'pineapple'])  # Adds multiple elements

# Removing elements
fruits.remove('banana')  # Removes first occurrence
last_item = fruits.pop()  # Removes and returns last element
specific_item = fruits.pop(1)  # Removes at specific index
fruits.clear()  # Removes all elements

# Analysis
print(fruits.count('apple'))  # Counts occurrences
print(fruits.index('banana'))  # Finds first index 

# Ordering
fruits.sort()  # Sorts in ascending order
fruits.sort(reverse=True)  # Sorts in descending order
fruits.reverse()  # Reverses order in-place

# Copying
new_fruits = fruits.copy()  # Creates a shallow copy
```

## 2. Tuples

Tuples are similar to lists but immutable - once created, they cannot be modified.

### Tuple Basics

```python
# Creating a tuple
coordinates = (10.5, 20.8, 30.1)
print(coordinates)  # (10.5, 20.8, 30.1)
print(type(coordinates))  # <class 'tuple'>

# Single-element tuple requires a comma
single_tuple = (42,)  # Without comma it's just a value in parentheses

# Tuple packing and unpacking
person = "John", 25, "Developer"  # Packing
name, age, job = person  # Unpacking

# Accessing elements (same as lists)
print(coordinates[0])  # 10.5
print(coordinates[-1])  # 30.1
print(coordinates[0:2])  # (10.5, 20.8)

# Iterating
for value in coordinates:
    print(value)
```

### Tuple Methods

Tuples have only two methods due to their immutability:

```python
data = (1, 2, 3, 2, 3, 1, 3)
print(data.count(3))  # 3 - number of occurrences of 3
print(data.index(2))  # 1 - index of first occurrence of 2
```

### Tuple Advantages

```python
# 1. Faster than lists
# 2. Protect data from accidental modification
# 3. Can be used as dictionary keys (lists cannot)
# 4. Named tuples for clearer code:

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

## 3. Sets

Sets are unordered collections with no duplicate elements.

### Set Basics

```python
# Creating a set
unique_fruits = {'apple', 'banana', 'cherry', 'apple'}
print(unique_fruits)  # {'banana', 'cherry', 'apple'} - notice duplicates are removed
print(type(unique_fruits))  # <class 'set'>

# Empty set (can't use {} as that creates an empty dict)
empty_set = set()

# Creating set from other collections
colors_list = ['red', 'blue', 'green', 'blue']
colors_set = set(colors_list)  # {'red', 'blue', 'green'}

# No indexing (unordered)
# print(unique_fruits[0])  # Error - sets don't support indexing

# Membership testing (very fast)
print('banana' in unique_fruits)  # True

# Iterating
for fruit in unique_fruits:
    print(fruit)  # Order may vary as sets are unordered
```

### Set Methods

```python
# Adding elements
unique_fruits.add('orange')  # Add a single element
unique_fruits.update(['mango', 'kiwi'])  # Add multiple elements

# Removing elements
unique_fruits.remove('banana')  # Raises error if not found
unique_fruits.discard('pear')  # No error if not found
popped_item = unique_fruits.pop()  # Removes and returns an arbitrary element
unique_fruits.clear()  # Removes all elements

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements from both sets)
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))  # Same result

# Intersection (elements common to both sets)
print(set1 & set2)  # {3, 4}
print(set1.intersection(set2))  # Same result

# Difference (elements in first set but not in second)
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))  # Same result

# Symmetric difference (elements in either set but not both)
print(set1 ^ set2)  # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))  # Same result

# Subset and superset
set3 = {3, 4}
print(set3.issubset(set1))  # True - all elements in set3 are in set1
print(set1.issuperset(set3))  # True - set1 contains all elements in set3
print(set1.isdisjoint(set3))  # False - sets have common elements
```

## Choosing the Right Collection Type

| Collection | Order | Mutability | Duplicates | Use Case |
|------------|-------|------------|------------|----------|
| List | ✓ | Mutable | ✓ | Sequence of items that might change |
| Tuple | ✓ | Immutable | ✓ | Fixed sequence, dictionary keys, data integrity |
| Set | ✗ | Mutable | ✗ | Testing membership, removing duplicates, math operations |

## Performance Considerations

- Lists: Fast for appending/popping at end, slow for inserting/removing elsewhere
- Tuples: Slightly faster than lists for iteration and accessing elements
- Sets: Extremely fast for membership testing, union/intersections