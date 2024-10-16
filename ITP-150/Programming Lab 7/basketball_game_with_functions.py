"""
basketball_game_with_functions.py
@author: Sarah Williams
Date: 15 October 2024
Assignment: Lab 7 Basketball Game With Functions

Purpose: Simulate a 1v1 basketball game using nested for loops.
"""

import random

def main():
    counter = 0
    player1 = input_player_name("Player 1")
    player2 = input_player_name("Player 2")
    player1_score = 0
    player2_score = 0

    for i in range(4):
        print("--------------------------- Quarter ", (i + 1), "----------------------------")
        print(f"{"          "} {player1:<31s} {player2:<30s}")
        print(f"{"Shot #":8s} {"Shot":15s} {"Score":15s} \t\t{"  Shot":15s} {"Score":15s}")

        for j in range(720, 0, -30):
            player1_shot = random.randint(0, 3)
            player2_shot = random.randint(0, 3)
            counter = counter + 1
            player1_shotmade = determine_player_shotmade(player1_shot)
            player2_shotmade = determine_player_shotmade(player2_shot)
            player1_score = calculate_score(player1_score, player1_shot)
            player2_score = calculate_score(player2_score, player2_shot)
            print(f"{counter:<8d} {player1_shotmade:<15s} {player1_score:<15d}\
                  {player2_shotmade:<15s} {player2_score:<15d}")
    display_winner(player1_score, player2_score, player1, player2)

def input_player_name(player):
    print("Please enter the ", player, "name: ")
    player_name = input()
    return player_name

def determine_player_shotmade(player_shot):
    if player_shot == 0:
        player_shotmade = "Air Ball"
    elif player_shot == 1:
        player_shotmade = "Free Throw"
    elif player_shot == 2:
        player_shotmade = "Two Pointer"
    else:
        player_shotmade = "Three Pointer"
    return player_shotmade

def calculate_score(player_score, player_shot):
    player_score = player_score + player_shot
    return player_score

def display_winner(player1_score, player2_score, player1, player2):
    if player1_score > player2_score:
        print(player1, " bringing a W!")
    elif player2_score > player1_score:
        print(player2, " bringing a W!")
    else:
        print("Tie Game! Go home...see you later!")

if __name__ == "__main__":
    main()