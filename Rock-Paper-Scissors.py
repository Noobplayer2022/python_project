print("/////cpu2 is a person who want to win . a person that i'm want to win is cpu2 wich calld cpu2player . you have only 3 round to make cpu2 win or you lose///// ")

import random

while True:

 choices=["rock","paper","scissors"]

 cpu2player=random.choice(choices)
 computer=random.choice(choices)



 if computer==cpu2player:
     print("computer:",computer)
     print("cpu2player:",cpu2player)
     print("tie!")
 elif cpu2player=="rock":
     if computer=="paper":
         print("computer:", computer)
         print("cpu2player:", cpu2player)
         print("you lose")
     if computer == "scissors":
         print("computer:",computer)
         print("cpu2player:", cpu2player)
         print("you win!")

 elif cpu2player=="paper":
     if computer=="scissors":
         print("computer:", computer)
         print("cpu2player:", cpu2player)
         print("you lose!")
     if computer == "rock":
         print("computer:",computer)
         print("cpu2player:", cpu2player)
         print("you win!")

 elif cpu2player=="scissors":
     if computer=="paper":
         print("computer:", computer)
         print("cpu2player:", cpu2player)
         print("you win!")


 play_again=input("do you want to play again (yes/no)?: ").lower()
 if play_again !="yes":
     break

print("bye")


