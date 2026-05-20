import random
numLoop=0
switch=False

while True:
    try:
        numLoop = int(input("How many times to run the simulation? "))

        if numLoop<=0:
            print("Please enter a positive number.")
            continue
        
        break
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
while True:
    switch = input("Would you like to switch? (Y/N): ").strip().lower()

    if switch[0] == "y":
        switch = True
        break
    else:
        switch=False
        break
        
winCounter=0
loseCounter=0
for i in range(numLoop):
    doors = [0,0,0,0,0]
    hostChoices = [0,1,2,3,4]
    playerChoices= [0,1,2,3,4]
    
    carIndex = random.randint(0,4)
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
    
    if switch:
        print("Player decided to pick again")
        playerPick=random.choice(playerChoices)
        print("Player chose door#"+str(playerPick+1))
    else:
        print("Player decided not to pick again")
    
    if(doors[playerPick]=="car"):
        winCounter+=1
        print("Win")
    else:
        loseCounter+=1
        print("Lose")
    
    print("")
   
print(f"Player won {winCounter} times")
print(f"Player lost {loseCounter} times")
    
    
    
    
    
    
    

  
        