import random

cChoice =random.choice(['rock', 'paper', 'scissor'])

def compChoice():
    cChoice =random.choice(['rock', 'paper', 'scissor'])

userChoice= input("Enter Rock(r/R)  Paper(p/P) or Scissor(s/S): ")
print(userChoice)
print(cChoice)


if(userChoice == cChoice):
    print("Its a tie")

elif(userChoice=="r" or userChoice =="R " and compChoice=="scissor" ):
    print("user wins")

elif(userChoice=="r" or userChoice =="R" and compChoice=="paper"):
    print("computer wins")

elif(userChoice=="p" or userChoice =="P" and compChoice=="scissor"):
    print("computer wins")

elif(userChoice=="p" or userChoice =="P" and compChoice=="rock"):
    print("user wins")

elif(userChoice=="s" or userChoice =="S" and compChoice=="rock"):
    print("computer wins")

elif(userChoice=="s" or userChoice =="S" and compChoice=="paper"):
    print("user wins")
    


