import random

print("Welcome to Dice Rolling Simulator!")
choice = input("Do you wanna play? (y / n):")

while (choice == 'y'):
    
    num = random.randint(1,6)
    print("The dice is rolling...")
    
    if num == 1:
        print(" ---------- ")
        print("|          |")
        print("|    0     |")
        print("|          |")
        print(" ---------- ")

    elif num == 2:
        print(" ---------- ")
        print("|          |")
        print("|    0 0   |")
        print("|          |")
        print(" ---------- ")
    
    elif num == 3:
        print(" ---------- ")
        print("|          |")
        print("|   0 0 0  |")
        print("|          |")
        print(" ---------- ")

    elif num == 4:
        print(" ---------- ")
        print("|          |")
        print("|    0 0   |")
        print("|    0 0   |")
        print("|          |")
        print(" ---------- ")

    elif num == 5:
        print(" ---------- ")
        print("|          |")
        print("|    0 0   |")
        print("|   0 0 0  |")
        print("|          |")
        print(" ---------- ")
    
    else:
        print(" ---------- ")
        print("|    0 0   |")
        print("|    0 0   |")
        print("|    0 0   |")
        print(" ---------- ")
        
    choice = input("Do you wanna play? (y / n):")


if choice == 'n':
    exit()