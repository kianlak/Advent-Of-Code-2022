# Calculates the number of trees that are visibile from outside the grid

def part2():
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
            if (x == (ROW - 1)) or (forest_grid[x][column] >= tree_house_height): # Tree search reaches the edge
                return x - row    
        return x - row

    # Checks upwards
    def check_row_up(row, column, tree_house_height, forest_grid):
        for x in reversed(range(row)):
            if (x == 0) or (forest_grid[x][column] >= tree_house_height): # Tree search reaches the edge
                return row - x    
        return row - x

    # Checks to the right
    def check_column_right(row, column, tree_house_height, forest_grid):        
        for y in range(column + 1, COLUMN, 1):
            if (y == (COLUMN - 1)) or (forest_grid[row][y] >= tree_house_height): # Tree search reaches the edge
                return y - column   
        return y - column
    
    # Checks to the left
    def check_column_left(row, column, tree_house_height, forest_grid):
        for y in reversed(range(column)):            
            if (y == 0) or (forest_grid[row][y] >= tree_house_height): # Tree search reaches the edge
                return column - y    
        return column - y

# === Helper Functions End === #

    # Program Start #
    with open('forest_map.txt') as file:
        forest_grid = grid_setup(forest_grid)
        most_scenic_spot = 0
        for x in range(ROW):
            for y in range(COLUMN):
                if not ((x == 0) or (y == 0) or (x == (ROW - 1)) or (y == (COLUMN - 1))):
                    tree_house_height = forest_grid[x][y]    # Spot from which we are comparing other tree heights
                    
                    down_view = check_row_down(x, y, tree_house_height,forest_grid)
                    up_view = check_row_up(x, y, tree_house_height,forest_grid)
                    left_view = check_column_left(x, y, tree_house_height,forest_grid)
                    right_view = check_column_right(x, y, tree_house_height,forest_grid)
                    
                    if most_scenic_spot < (down_view * up_view * left_view * right_view):
                        most_scenic_spot = down_view * up_view * left_view * right_view
        
        print("Most scenic spot has", most_scenic_spot, "trees visible")