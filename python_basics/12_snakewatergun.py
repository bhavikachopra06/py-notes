# Snake Water Gun Game
# Snake vs Water -> Snake wins
# Water vs Gun -> Water wins
# Gun vs Snake -> Gun wins

import random
computer = random.choice([1,0,-1]) 
user = input("Enter snake,water,gun: ") 
user_dict = {"s":1, "w":-1, "g":0} 
reverse_dict = {1:"snake", -1:"water", 0:"gun"}
user_num = user_dict[user]

print(f"You Chose {reverse_dict[user_num]}\nComputer chose {reverse_dict[computer]}")

if(user_num == computer):
    print("Tie")
else:
    if(user_num == 1 and computer == 0):
        print("You win!")
    elif(user_num == 1 and computer == -1):
        print("You win!")
    elif(user_num == 0 and computer == -1):
        print("You lose! BOOOOO")
    elif(user_num == 0 and computer == 1):
        print("You win!")
    elif(user_num == -1 and computer == 1):
        print("You lose! BOOOOO")
    elif(user_num == -1 and computer == 0):
        print("You win!")
    else:
        print("Something went wrong")

    
