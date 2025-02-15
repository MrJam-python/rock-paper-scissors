import random
print ("-------------------------------------------------------------")
print ("Welcome To Rock, Paper, Scissors!")
print ("-------------------------------------------------------------")



while True:
    player_choice=input ("Choose Rock, Paper, Or Scissors.")
    cpu_choice= random.choice(["rock","paper","scissors"])
    print("You picked " + player_choice)
    print("The computer picked " + cpu_choice)

    if player_choice == cpu_choice:
        print("You Tied!") 
     
    if player_choice=="rock" and cpu_choice== "paper":
        print("You Lost!")
    
    if player_choice=="rock" and cpu_choice== "scissors":
        print("You Won!")
    
    if player_choice=="paper" and cpu_choice== "scissors":
        print("You Lost!")
    
    if player_choice=="paper" and cpu_choice== "rock":
        print("You Won!")
    
    if player_choice=="scissors" and cpu_choice== "rock":
        print("You Lost!")
    
    if player_choice=="scissors" and cpu_choice== "paper":
        print("You Won!")
