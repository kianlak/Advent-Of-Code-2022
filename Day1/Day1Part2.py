# This will display the most calories carried by the top 3 elves and add the total together

def part2():
    total_calories = 0
    
    # Read calories from each elf
    with open('elves_carried_calories.txt') as file:
        most_calories = [0, 0, 0]   # Top 3 most calories found
        current_calories = 0        # Current calories in calculation
        
        # Goes through each line to check if it's empty or not
        for line in file.readlines():
            
            # Check to see if line is empty or not, if it isn't,
            # keep adding calories onto current_calories.
            # If Line is empty, check to see if there is a 
            # contending calorie for the top 3 elves calories
            # and then reset calculations
            if line.strip():
                current_calories += int(line)
            else:
                # Checks to see if minimum value from most_calories
                # can be replaced with a larger calorie number
                if current_calories > min(most_calories):
                    most_calories[most_calories.index(min(most_calories))] = current_calories   # Replacing the current 3rd highest calories from the list with current_calories
                    current_calories = 0
                else:
                    current_calories = 0

    for x in range(3):
        total_calories += most_calories[x]
    
    most_calories.sort(reverse=True)    # Setting the list in descending order
    
    print("Top 3 calories carried by elves:\n#1 Elf: "
          + str(most_calories[0]) + " calories\n#2 Elf: "
          + str(most_calories[1]) + " calories\n#3 Elf: "
          + str(most_calories[2]) + " calories\n"
          + "Total amount of calories carried by the top 3 elves is: "
          + str(total_calories))
