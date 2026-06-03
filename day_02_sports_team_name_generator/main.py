print(r'''

                 -|
               -' |
             -'   | __().
        ==wkm=====|'\/   `.O__
                            \ `,
                           _-^.
                           `.  `---,
                             :



       ____________________________________
       ///\\\///\\\///\\\///\\\///\\\///\\\
''')
print("Welcome to The State Championship.")
print("Your mission is to win the championship.")

choice1 = input("Do you want to go down the right side or left side of the court? Enter right or left: \n")

#Continue on in the game
if choice1 == "right":
    print("You spin moved passed a defender, and made it passed half court.")

    choice2 = input("Do you want to dunk, pass or shoot a 3. Type dunk,pass or shoot. \n")

    if choice2 == "pass":
        print("You were able to pass the ball to your teammate wide open!")
    elif choice2 == "shoot":
        print("You shot the ball and missed!")
    else:
        print("You lost the championship.")
        exit()

    choice3 = input("Your team missed, but your team recovered and got the rebound. Do you call for a pass or do nothing? Type pass or nothing. \n")
    if choice3 == "pass":
        print("You called the pass and got it!")
    else:
        print("You lost the championship.")
        exit()

    choice4= input("Now do you shoot the 3 or go for the dunk? Type dunk or 3\n")
    if choice3 == "dunk":
        print("You went in for the dunk, and your team won the championship!")
    else:
        print("You shot the ball and missed! You lost the championship.")
        exit()

    print("You won the championship!")

#Game Over
else:
    print("You were injured coming down the court.You lost the championship.")
