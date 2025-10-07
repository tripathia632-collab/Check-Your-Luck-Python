import random

print("Lets chech your luck")

name = input("What is your name: ")

answer = random.randint(1, 3)
if answer == 1:
    print(f"Hello {name}, you are lucky")
elif answer == 2:
    print(f"Hello {name}, you are unlucky") 
else:
    print(f"Hello {name}, you are average")