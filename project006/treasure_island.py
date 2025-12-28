from random import choice

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the treasure island. \n Your mission is find the treasure.")
choice1 = input("You're at the cross road do you want to go?\n Type left or right: ")
if choice1 == "left":
    choice2 = input("You’ve arrived at a lake!!!\n Type wait or swim: ")
    if choice2 == "wait":
        choice3 = input("You’ve arrived the island unharmed.!!! There's house with three doors\n Type red, blue or green: ")
        if choice3 == "blue":
            print("You've found the treasure!!! Congratulations!")
        elif choice3 == "red":
            print("you've entered the room filled with crocodiles. Game Over")
        else:
            print("It's a room full of fire. Game Over")
    else: print("You got attached by alien. Game Over")
else:
    print("you fell into a hole. Game Over")

