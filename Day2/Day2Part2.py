from enum import Enum
import re

# This function is used to calculate a winner between the elf and yourself
# so we make use of the enum values to create a set formula in which
# we can quickly check who draws, wins, or loses
def compare_choices(elf_choice, round_end_type):
    class ElfChoicePoints(Enum):
        A = 1
        B = 2
        C = 3

    class RoundEndType(Enum):
        X = 0
        Y = 3
        Z = 6
    
    elf_choice_value = ElfChoicePoints[elf_choice].value
    round_end_type_value = RoundEndType[round_end_type].value
    
    # Refer to main.py lines [9-42] for an explanation for this algorithm
    # Draw
    if round_end_type_value == 3:
        return (elf_choice_value) + round_end_type_value
    # Win
    elif round_end_type_value == 6:
        if elf_choice_value == 3:
            return (elf_choice_value - 2) + round_end_type_value
        else:
            return (elf_choice_value + 1) + round_end_type_value
    # Loss
    else:
        if elf_choice_value == 1:
            return (elf_choice_value + 2)
        else:
            return (elf_choice_value - 1)

# This will return the total points that you have after
# following the elf's strategy guide

def part2():
    your_total_points = 0   # Your Points
    
    # Read instructions from instructions.txt
    with open('strategy_guide.txt') as file:
        for line in file.readlines():
            
            # Extracting choices from strategy guide
            elf_choice = re.findall(r'[A-C]', line)[0]
            round_end_type = re.findall(r'[X-Z]', line)[0]
            
            your_points = compare_choices(elf_choice, round_end_type)
            
            your_total_points += your_points
    
    print("You scored: " + str(your_total_points) + " points")