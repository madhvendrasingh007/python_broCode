#collection -> single variable using to store multiple values
    #list  [] -> ordered, mutable, allows duplicates
    #tuple {} -> ordered, immutable, allows duplicates
    #set   () -> unordered, mutable, no duplicates

fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(type(fruits))
print(fruits[0]) # first element
print(fruits[::-1]) # reverse order

for f in fruits:
    print(f) # print each element

# print(dir(fruits)) # print all attributes and methods of the list
# print(help(fruits)) # print help for the list

print('banana' in fruits) # check if 'banana' is in the list

# list methods
print(fruits.count('apple')) # count the number of times 'apple' appears in the list
print(fruits.index('banana')) # find the index of 'banana' in the list
print(fruits.append('orange')) # add 'orange' to the end of the list
print(fruits) # print the list after adding 'orange'

print(fruits.insert(1, 'kiwi')) # insert 'kiwi' at index 1
print(fruits) # print the list after inserting 'kiwi'
print(fruits.remove('banana')) # remove 'banana' from the list
print(fruits) # print the list after removing 'banana'
print(fruits.pop()) # remove and return the last element of the list
print(fruits) # print the list after popping the last element

print(fruits.sort()) # sort the list in ascending order
print(fruits) # print the sorted list
print(fruits.reverse()) # reverse the order of the list
print(fruits) # print the reversed list