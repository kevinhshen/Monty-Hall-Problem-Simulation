import random
numLoop=0
pickAgain=True

while True:
    try:
        numLoop = int(input("How many times to run the simulation? "))

        if numLoop<=0:
            print("Please enter a positive number.")
            continue
        
        break
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
        

     
winCounter=0
loseCounter=0
for i in range(numLoop):
    doors = [0,0,0]
    hostChoices = [0,1,2]
    playerChoices= [0,1,2]
    
    carIndex = random.randint(0,2)
    hostChoices.remove(carIndex)
    doors[carIndex] = "car"
    #there are 3 doors, the car is randomly placed behind one
    
    playerPick = random.choice(playerChoices)
    playerChoices.remove(playerPick)
    if(playerPick!=carIndex):
        hostChoices.remove(playerPick)
    print("Player picked door #"+str(playerPick+1))
    
    hostPick = random.choice(hostChoices)
    hostChoices.remove(hostPick)
    playerChoices.remove(hostPick)
    print("Host revealed nothing behind door #"+str(hostPick+1))
    
    if pickAgain:
        print("Player decided to pick again")
        playerPick=random.choice(playerChoices)
        print("Player chose door#"+str(playerPick))
    else:
        print("Player decided not to pick again")
    
    if(doors[playerPick]=="car"):
        winCounter+=1
    else:
        loseCounter+=1
   
print(f"Player won {winCounter} times")
print(f"Player lost {loseCounter} times")
    
    
    
    
    
    
    

  
        