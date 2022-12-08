import re

# Prints out how many fully containing tasks are found

def part1():
    with open('assignments.txt') as file:
        full_contain_total = 0  # Keeps track of how many full_contains that have been found
        
        for line in file.readlines():
            elf1_min_range, elf1_max_range, elf2_min_range, elf2_max_range = re.findall(r'\d+', line)  # Extract necessary values to respective variables
            
            # Casts all ranges as integers
            elf1_min_range, elf2_min_range, elf1_max_range, elf2_max_range = int(elf1_min_range), int(elf2_min_range), int(elf1_max_range), int(elf2_max_range)
            
            # Checks to see whether the first elf or the second elf have the containing range
            if((elf1_min_range <= elf2_min_range) and (elf1_max_range >= elf2_max_range) or (elf1_min_range >= elf2_min_range) and (elf1_max_range <= elf2_max_range)):
                full_contain_total += 1
                
        print("The number of fully containing tasks is: " + str(full_contain_total))
                    
                       