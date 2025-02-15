import random
print ("------------------------------------------------------------------------------------------------------------------------------")
print ("Welcome To Rock, Paper, Scissors!")
print ("------------------------------------------------------------------------------------------------------------------------------")
player_choice=input ("Choose Rock, Paper, Or Scissors.")
cpu_choice= random.randint(1,3)
if player_choice=="rock" and cpu_choice== 2:
    print ("You Lost!")
