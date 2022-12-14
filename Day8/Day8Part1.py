# Calculates the number of trees that are visibile from outside the grid

def part1():
    ROW, COLUMN = [99, 99]                      # Dimensions for the forest map
    forest_grid = [[] for _ in range(COLUMN)]   # Forest map represented by a 2D Array (99x99)
    trees_visible = 0                           # Number of trees visible

# === Helper Functions Start === #    
    
    # Inserts tree heights into forest_grid
    def grid_setup(forest_grid):
        for row, line in enumerate(file):
            for tree_height in line.strip():
                forest_grid[row].append(int(tree_height))
        return forest_grid

    # Checks downwards
    def check_row_down(row, column, tree_house_height, forest_grid):
        for x in range(row + 1, ROW, 1):
            if((forest_grid[x][column] < tree_house_height) and (x == (ROW - 1))):  # Tree search reaches the edge
                return True
            elif(forest_grid[x][column] >= tree_house_height):                      # Tree gets blocked
                return False

    # Checks upwards
    def check_row_up(row, column, tree_house_height, forest_grid):
        for x in reversed(range(row)):
            if((forest_grid[x][column] < tree_house_height) and (x == 0)):  # Tree search reaches the edge
                return True
            elif(forest_grid[x][column] >= tree_house_height):              # Tree gets blocked
                return False


    # Checks to the right
    def check_column_right(row, column, tree_house_height, forest_grid):        
        for y in range(column + 1, COLUMN, 1):
            if((forest_grid[row][y] < tree_house_height) and (y == (COLUMN - 1))):  # Tree search reaches the edge
                return True
            elif(forest_grid[row][y] >= tree_house_height):                         # Tree gets blocked
                return False
    
    # Checks to the left
    def check_column_left(row, column, tree_house_height, forest_grid):
        for y in reversed(range(column)):            
            if((forest_grid[row][y] < tree_house_height) and (y == 0)): # Tree search reaches the edge
                return True
            elif(forest_grid[row][y] >= tree_house_height):             # Tree gets blocked
                return False

# === Helper Functions End === #

    # Program Start #
    with open('forest_map.txt') as file:
        forest_grid = grid_setup(forest_grid)
        
        for x in range(ROW):
            for y in range(COLUMN):
                if((x == 0) or (y == 0) or (x == (ROW - 1)) or (y == (COLUMN - 1))):
                    trees_visible += 1
                else:
                    tree_house_height = forest_grid[x][y]    # Spot from which we are comparing other tree heights
                    
                    # Checks to see if a tree would be visible from any direction
                    if (check_row_down(x, y, tree_house_height,forest_grid) or (check_row_up(x, y, tree_house_height,forest_grid)) or (check_column_left(x, y, tree_house_height,forest_grid)) or (check_column_right(x, y, tree_house_height,forest_grid))):
                        trees_visible += 1
        print(trees_visible, "trees are visible")