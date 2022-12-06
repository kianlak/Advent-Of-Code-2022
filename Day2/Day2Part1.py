from enum import Enum
import re

# This function is used to calculate a winner between the elf and yourself
# so we make use of the enum values to create a set formula in which
# we can quickly check who draws, wins, or loses
def compare_choices(elf_choice, your_choice):
    class ElfChoicePoints(Enum):
        A = 1
        B = 2
        C = 3

    class YourChoicePoints(Enum):
        X = 1
        Y = 2
        Z = 3

    elf_choice_value = ElfChoicePoints[elf_choice].value
    your_choice_value = YourChoicePoints[your_choice].value

    outcome = elf_choice_value - your_choice_value
    
    # Checks for a Draw, Win, or Loss respectively
    # Refer to main.py lines [9-42] for an explanation for this algorithm
    if outcome == 0:                    # Draw
        return (your_choice_value + 3)
    elif outcome == 2 or outcome == -1: # Win
        return (your_choice_value + 6)
    else:                               # Loss
        return (your_choice_value)
   
# This will return the total points that you have after
# following the elf's strategy guide

def part1():
    your_total_points = 0   # Your Points
    
    with open('strategy_guide.txt') as file:
        for line in file.readlines():
            
            # Extracting choices from strategy guide
            elf_choice = re.findall(r'[A-C]', line)[0]
            your_choice = re.findall(r'[X-Z]', line)[0]
            
            your_points = compare_choices(elf_choice, your_choice)
            
            your_total_points += your_points
    
    print("You scored: " + str(your_total_points) + " points")