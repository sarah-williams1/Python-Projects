"""
Author: Sarah Williams
Date: 26 September 2024
Assignment: Project 2: Field Goals
"""

def validate_player_count():
    for input_value in player_count:
        if input_value in range (1, 51):
            break
        else:
            print(f"{input_value} is not valid. Players entered must be between 1 and 50.")
        break
def validate_field_goals():
    for input_value in field_goals:
        if input_value in range (1, 151):
            break
        else:
            print(f"{field_goals} is invalid. Please enter a value between 1 and 150.")
        break
    

print("Please enter the number of players (between 1 and 50): ")
player_count = int(input())
validate_player_count()

player_name = input()
print(f"Please enter the team for {player_name}: ")
team_name = input()
print("Please enter the number of field goals made (between 1 and 150): ")
field_goals = int(input())
validate_field_goals()


    