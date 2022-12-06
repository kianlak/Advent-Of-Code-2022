import string

# Calculates the sum_of_priorities based on what exists in the rucksacks list

def part1():
    with open('rucksacks.txt') as file:
        sum_of_priorities = 0
        
        for line in file.readlines():
            found_items = []    # Used to keep track of what items are found currently in both of the given compartments
            compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]   # Splits up into two compartments

            # Puts every item that exists in both compartments into found_items
            for x in range(len(compartment1)):
                if (compartment1[x] in compartment2) and (compartment1[x] not in found_items):
                    found_items.append(compartment1[x])
            
            # Calculates total priorty of all found_items
            for x in range(len(found_items)):
                sum_of_priorities += string.ascii_letters.index(found_items[0]) + 1
            
    
    print("The total sum of priorities is: " + str(sum_of_priorities))