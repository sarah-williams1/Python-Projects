"""
Author: Sarah Williams
Date: 05 October 2024
Assignment: Lab 4: Basektball Game
"""

import random
counter = 0

player1 = input("Please enter the name for Player1:\n")
player2 = input("Please enter the name for Player2:\n")
player1_score = 0
player2_score = 0

 
for i in range(4): 
    print("--------------------------- Quarter ", (i + 1), "------------------------")
    print(f'{" "} {player1:<31s} {player2:<30s}')
    print(f'{"Shot #":8s} {"Shot":15s} {"Score":15s} {"Shot":15s} {"Score":15s}')

for j in range(720, 0, -30):
    player1_shot = random.randint(0, 3)
    player2_shot = random.randint(0, 3)
    counter = counter + 1

    if player1_shot == 0:
        player1_shotmade = "Air Ball"
    elif player1_shot == 1:
        player1_shotmade = "Free Throw"
    elif player1_shot == 2:
        player1_shotmade = "Two Pointer"
    else:
        player1_shotmade = "Three Pointer"

    if player2_shot == 0:
        player2_shotmade = "Air Ball"
    elif player2_shot == 1:
        player2_shotmade = "Free Throw"
    elif player2_shot == 2:
        player2_shotmade = "Two Pointer"
    else:
        player2_shotmade = "Three Pointer"

    player1_score = player1_score + player1_shot
    player2_score = player2_score + player2_shot

print(f'{counter:<8d} {player1_shotmade:<15s} {player1_score:<15d} \
       {player2_shotmade:<15s} {player2_score:<15d}')

if player1_score > player2_score:
    print(player1, " bringing a W!")
elif player2_score > player1_score:
    print(player2, " bringing a W!")
else:
    print("Tie Game..Go Home..See ya' later!")