# This will display the most calories carried by an elf

def part1():
    # Read calories from each elf
    with open('carried_calories.txt') as file:
        most_calories = 0       # Most calories found
        current_calories = 0    # Current calories in calculation
        
        # Goes through each line to check if it's empty or not
        for line in file.readlines():
            
            # Check to see if line is empty or not, if it isn't,
            # keep adding calories onto current_calories.
            # If Line is empty, check to see if there is a 
            # contending calorie amount
            if line.strip():
                current_calories += int(line)
            else:
                # Check to see if there are more calories than most_calories
                # and then reset current_calories for next calculations
                if current_calories > most_calories:
                    most_calories = current_calories
                    current_calories = 0
                else:
                    current_calories = 0
                    
    print("Elf carrying the most calories has: " + str(most_calories) + " calories")
