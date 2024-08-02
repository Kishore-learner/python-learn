# Create a program capable of greeting you bu accessing time module
import time
hour = time.strftime("%H")

if hour >= 20 or hour < 4:
    print("Good night")
elif 4 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 17:
    print("Good afternoon")
else:
    print("Good evening")
