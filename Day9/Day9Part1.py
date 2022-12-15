import re

def part1():
    # === Helper Functions Start === #
        
    # Makes head travel left with tail
    def left_travel(hx, hy, tx, ty, traveled, num_steps):
        for _ in range(num_steps):
            hx -= 1 # Traveling left
            
            if (abs(hx - tx) > 1) or (abs(hy - ty) > 1):
                # Shifting tail coordinates to previous heads coordinates
                tx = hx + 1
                ty = hy
                
                # Tail traveled to new unique spot
                if [tx, ty] not in traveled:
                    traveled.append([tx, ty])
        return hx, hy, tx, ty, traveled
    
    # Makes head travel right with tail
    def right_travel(hx, hy, tx, ty, traveled, num_steps):
        for _ in range(num_steps):
            hx += 1 # Traveling right
            
            if (abs(hx - tx) > 1) or (abs(hy - ty) > 1):
                # Shifting tail coordinates to previous heads coordinates
                tx = hx - 1
                ty = hy
                
                # Tail traveled to new unique spot
                if [tx, ty] not in traveled:
                    traveled.append([tx, ty]) 
        return hx, hy, tx, ty, traveled

    # Makes head travel upwards with tail
    def up_travel(hx, hy, tx, ty, traveled, num_steps):
        for _ in range(num_steps):
            hy -= 1 # Traveling right
            
            if (abs(hx - tx) > 1) or (abs(hy - ty) > 1):
                # Shifting tail coordinates to previous heads coordinates
                tx = hx
                ty = hy + 1
                
                # Tail traveled to new unique spot
                if [tx, ty] not in traveled:
                    traveled.append([tx, ty]) 
        return hx, hy, tx, ty, traveled

    # Makes head travel downwards with tail
    def down_travel(hx, hy, tx, ty, traveled, num_steps):
        for _ in range(num_steps):
            hy += 1 # Traveling right
            
            if (abs(hx - tx) > 1) or (abs(hy - ty) > 1):
                # Shifting tail coordinates to previous heads coordinates
                tx = hx
                ty = hy - 1
                
                # Tail traveled to new unique spot
                if [tx, ty] not in traveled:
                    traveled.append([tx, ty]) 
        return hx, hy, tx, ty, traveled
    
    # === Helper Functions End === #   
    
    with open("path.txt") as file:
        head_x, head_y = [0, 0]     # Holds coordinates of the head
        tail_x, tail_y = [0, 0]     # Holds coordinates of the tail
        spots_traveled = [[0, 0]]   # Holds unique coordinates the tail traveled to 
    
        # Program Start
        for line in file.readlines():
            
            # Read an separate direction and number of steps
            match = re.match(r'([A-Z]) (\d+)', line.strip())
            direction, number_of_steps = match.group(1), int(match.group(2))
                                    
            # Travel in specified directions
            if direction == 'L':
                head_x, head_y, tail_x, tail_y, spots_traveled = left_travel(head_x, head_y, tail_x, tail_y, spots_traveled, number_of_steps)
            elif direction == 'R':
                head_x, head_y, tail_x, tail_y, spots_traveled = right_travel(head_x, head_y, tail_x, tail_y, spots_traveled, number_of_steps)
            elif direction == 'U':
                head_x, head_y, tail_x, tail_y, spots_traveled = up_travel(head_x, head_y, tail_x, tail_y, spots_traveled, number_of_steps)
            elif direction == 'D':
                head_x, head_y, tail_x, tail_y, spots_traveled = down_travel(head_x, head_y, tail_x, tail_y, spots_traveled, number_of_steps)
                
    print(len(spots_traveled))