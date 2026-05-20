The Monty Hall Problem is a famous probability problem.
This program aims to simulate and prove the Monty Hall problem, showing the interesting real life application of probability.

Explaination:
Here are 3 doors: [0,0,0]
The "car" is placed randomly behind 1 of the door: [0,"car",0]

Player has two different possibilities:
Option 1 (67%): Player pick door #1 or #3 (the empty doors)
    For example: Player picked door #1
    The host revealed nothing behind door #3
    Player will 100% if he switch
    Thus, under the assumption that player would switch when host revealed the empty door, player's 67% chance to lose turns into 100% win
    
Option 2 (33%): Player picked the right door
    If player pick again, they 100% lose


Summary: Think in terms of a boolean, the act of switching "flip" player's odds of winning. The same is true for the opposite.


