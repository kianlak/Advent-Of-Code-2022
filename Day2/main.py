import sys
sys.dont_write_bytecode = True # Removes pycache from generating
from Day2Part1 import *
from Day2Part2 import *

part1()
part2()

# This is a more complicated solution as I continuously refer to this general formula for my solution:
# For Elf:
# Rock = A = 1
# Paper = B = 2
# Scissors = C = 3
# 
# For You:
# Rock = X = 1
# Paper = Y = 2
# Scissors = Z = 3
# 
# Formula below will expect the Elf's Choice on the RHS (Right Hand Side)
# and our Choice on the LHS (Left Hand Side)


# Draws for Us:
# Rock - Rock => 1 - 1 = 0
# Paper - Paper => 2 - 2 = 0
# Scissors - Scissors => 3 - 3 = 0
# In all cases for drawing, we will expect a 0


# Wins for Us:
# Rock - Paper => 1 - 2 = -1
# Paper - Scissors => 2 - 3 = -1
# Scissors - Rock => 3 - 1 = 2
# In all cases except for the last, we expect a -1


# Losses for Us:
# Rock - Scissors => 1 - 3 = -2
# Paper - Rock => 2 - 1 = 1
# Scissors - Paper => 3 - 2 = 1
# In all cases except for the first, we expect a 1