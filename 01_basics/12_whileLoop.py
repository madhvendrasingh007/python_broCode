# while loop -> it executes a block of code as long as a specified condition is true


food = input("Enter a food (q to quit): ")

while not food == "q":
    print(f"You like: {food}")
    food = input("Enter another food (q to quit): ")

print("bye!")
# The while loop will continue to ask for food until the user enters "q"