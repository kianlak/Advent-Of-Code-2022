import re

# This will move crates based on the instructions one by one

def part1(crate_stacks, top_crates):
    # Read instructions from instructions.txt
    with open('instructions.txt') as file:
        for line in file.readlines():
            num_crate, from_stack, to_stack = re.findall(r'\d+', line)  # Extract necessary values to respective variables          
            num_crate, from_stack, to_stack = int(num_crate), int(from_stack) - 1, int(to_stack) - 1
                    
            for x in range(num_crate):
                crate_stacks[to_stack].append(crate_stacks[from_stack].pop())   # Take each crate off a stack and put 
                                                                                # them onto another stack
           
    # Generates message for the elves                                                                     
    for x in range(9):
        top_crates += crate_stacks[x].pop()

    print("Message for the elves: " + top_crates)