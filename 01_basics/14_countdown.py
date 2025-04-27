import time

myTime = int(input("Enter the time in seconds: "))
for x in range(myTime, 0, -1):
    Sec = x%60
    Min = int(x/60)%60
    Hour = int(x/3600)%24
    print(f"{Hour:02}:{Min:02}:{Sec:02}")
    time.sleep(1)
print("Time's up!")
# This program takes a number of seconds as input and counts down to zero, printing each second as it goes.
# It uses the time.sleep() function to pause for one second between each print statement.