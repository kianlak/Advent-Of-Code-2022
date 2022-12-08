import re

# Prints out how many overlapping tasks are found

def part2():
    with open('assignments.txt') as file:
        overlapping_total = 0  # Keeps track of how many overlaps have been found
        
        for line in file.readlines():
            elf1_min_range, elf1_max_range, elf2_min_range, elf2_max_range = re.findall(r'\d+', line)  # Extract necessary values to respective variables
            
            # Casts all ranges as integers
            elf1_min_range, elf2_min_range, elf1_max_range, elf2_max_range = int(elf1_min_range), int(elf2_min_range), int(elf1_max_range), int(elf2_max_range)
            
            # Checks for overlapping ranges and fully containing ranges
            if(((elf1_min_range >= elf2_min_range) and (elf1_min_range <= elf2_max_range)) or ((elf2_min_range >= elf1_min_range) and (elf2_min_range <= elf1_max_range))):
                overlapping_total += 1

        print("There are " + str(overlapping_total) + " overlapping tasks")
                    
                       