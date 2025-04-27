# Variable = Sring, int, float, bool

first_name = "Kevin"
last_name = "Robinson"
age = 30
height = 5.9
is_student = True

print(f"Hello, my name is {first_name} {last_name} and I am {age} years old.")
print(f"My height is {height} feet and it is {is_student} that I am a student.")

print(type(first_name)) # str
print(type(last_name))  # str
print(type(age))        # int
print(type(height)) # float 
print(type(is_student)) # bool

print("first_name" + first_name) # first_nameKevin
print("age" + age) # age30
# This will cause an error because you cannot concatenate a string with an integer
# To fix this, you can convert the integer to a string using str()
# Corrected line
print("age" + str(age)) # age30
# You can also use f-strings to format the output   
print(f"age {age}") # age 30
# You can also use the format() method to format the output
print("age {}".format(age)) # age 30
# You can also use the % operator to format the output
print("age %d" % age) # age 30