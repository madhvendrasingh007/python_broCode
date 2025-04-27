#if condition
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else condition
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested if condition
if age >= 18:
    print("You are an adult.")
    if age < 65:
        print("You are a working adult.")
    else:
        print("You are a senior citizen.")