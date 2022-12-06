import re

# This will take multiple crates and move them at once

def part2(crate_stacks, top_crates):
    with open('instructions.txt') as file:
        for line in file.readlines():
            num_crate, from_stack, to_stack = re.findall(r'\d+', line)  # Extract necessary values to respective variables          
            num_crate, from_stack, to_stack = int(num_crate), int(from_stack) - 1, int(to_stack) - 1
            
            crate_in_order = [] # Use for holding the crates temporarily
            
            for x in range(num_crate):
                crate_in_order.append(crate_stacks[from_stack].pop())

            crate_in_order.reverse()                        # Reverse to put crates in order
            crate_stacks[to_stack].extend(crate_in_order)   # Merges crate_stacks[to_stack] with crate_in_order
   
    # Generates message for the elves                                                                     
    for x in range(9):
        top_crates += crate_stacks[x].pop()

    print("Message for the elves: " + top_crates)