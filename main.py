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
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        print("that option is not avaliable. Please choose another option.")
        counter -= 1
    
    elif player_choice == cpu_choice:
        print("You Tied This Round!")
       
     
    elif player_choice=="rock" and cpu_choice== "paper":
        print("You Lost The Round!")
        cpu_won+=1
        
    
    elif player_choice=="rock" and cpu_choice== "scissors":
        print("You Won The Round!")
        player_won+=1
        
    
    elif player_choice=="paper" and cpu_choice== "scissors":
        print("You Lost The Round!")
        cpu_won+=1
    
    elif player_choice=="paper" and cpu_choice== "rock":
        print("You Won The Round!")
        player_won+=1
    
    elif player_choice=="scissors" and cpu_choice== "rock":
        print("You Lost The Round!")
        cpu_won+=1
    
    elif player_choice=="scissors" and cpu_choice== "paper":
        print("You Won The Round!")
        player_won+=1
    counter += 1
    
print ("-------------------------------------------------------------")
print("The player won " + str(player_won) + " times!")
print("The computer won " + str(cpu_won) + " times!")
print ("-------------------------------------------------------------")
if player_won > cpu_won:
    print("The player won the game!")
elif player_won < cpu_won:
    print("The cpu won the game!")
elif player_won == cpu_won:
    print("The game resulted in a tie!")
