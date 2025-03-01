import random
player_won=0
cpu_won=0
print ("-------------------------------------------------------------")
print ("Welcome To Rock, Paper, Scissors!")
print ("-------------------------------------------------------------")

#A variable is a container that stores basic data
counter = 0 
while counter < 3:
    player_choice=input("Choose rock, paper, or scissors.")
    cpu_choice= random.choice(["rock","paper","scissors"])
    print("You picked " + player_choice)
    print("The computer picked " + cpu_choice)

    if player_choice == cpu_choice:
        print("You Tied!") 
     
    elif player_choice=="rock" and cpu_choice== "paper":
        print("You Lost!")
        cpu_won+=1
    
    elif player_choice=="rock" and cpu_choice== "scissors":
        print("You Won The Round!")
        player_won+=1
    
    elif player_choice=="paper" and cpu_choice== "scissors":
        print("You Lost!")
        cpu_won+=1
    
    elif player_choice=="paper" and cpu_choice== "rock":
        print("You Won!")
        player_won+=1
    
    elif player_choice=="scissors" and cpu_choice== "rock":
        print("You Lost!")
        cpu_won+=1
    
    elif player_choice=="scissors" and cpu_choice== "paper":
        print("You Won!")
        player_won+=1
    counter += 1
