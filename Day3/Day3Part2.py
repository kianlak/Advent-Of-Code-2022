import string

# Calculates the sum_of_priorities based on each groups badge identity

def part2():
    # Read rucksacks.txt
    with open('rucksacks.txt') as file:
        sum_of_priorities = 0
        grouped_rucksacks = []  # This will be used to group 3 rucksacks at a time for comparison
        
        for line in file.readlines():
            found_items = []                # Used to keep track of what items are found currently in the given rucksacks
            grouped_rucksacks.append(line)
            
            # When 3 rucksacks are found, begin looking for badge identity
            if len(grouped_rucksacks) == 3:
                
                # Puts every similar rucksack item in found_items to try to identify what their badges are
                for x in range(len(grouped_rucksacks[0])):
                    if(grouped_rucksacks[0][x] in grouped_rucksacks[1]) and (grouped_rucksacks[0][x] in grouped_rucksacks[2]) and (grouped_rucksacks[0][x] not in found_items) and (grouped_rucksacks[0][x] != '\n'):
                        found_items.append(grouped_rucksacks[0][x])
                
                grouped_rucksacks.clear()   # Clears groupred_rucksacks for next group
        
            # Calculates total priorty of all badge identity
            for x in range(len(found_items)):
                sum_of_priorities += string.ascii_letters.index(found_items[0]) + 1
            
    
    print("The total sum of priorities is: " + str(sum_of_priorities))