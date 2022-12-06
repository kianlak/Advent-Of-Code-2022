# This will display the most calories carried by the top 3 elves and add the total together

def part2():
    total_calories = 0
    
    # Read calories from each elf
    with open('carried_calories.txt') as file:
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
                if current_calories > most_calories[0]:     # Compared to #1 most calories
                    most_calories[2] = most_calories[1]
                    most_calories[1] = most_calories[0]
                    most_calories[0] = current_calories

                    current_calories = 0
                elif current_calories > most_calories[1]:   # Compared to #2 most calories                    
                    most_calories[2] = most_calories[1]
                    most_calories[1] = current_calories

                    current_calories = 0
                elif current_calories > most_calories[2]:   # Compared to #3 most calories
                    most_calories[2] = current_calories
                    current_calories = 0
                else:                                       # current_calories is too low
                    current_calories = 0
    
    for x in range(3):
        total_calories += most_calories[x]
    
    print("Top 3 calories carried by elves:\n#1 Elf: "
          + str(most_calories[0]) + " calories\n#2 Elf: "
          + str(most_calories[1]) + " calories\n#3 Elf: "
          + str(most_calories[2]) + " calories\n"
          + "Total amount of calories carried by the top 3 elves is: "
          + str(total_calories))
