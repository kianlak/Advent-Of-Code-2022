import sys
import copy
sys.dont_write_bytecode = True # Removes pycache from generating
from Day5Part1 import *
from Day5Part2 import *

# Setup data [lines 5 - 20]
original_crate_stacks = []  # List of stacks
crate_stacks = []           # List of stacks to be passed down functionss
top_crates = ""             # Top crates at the end of the instruction set

for x in range(9):
    original_crate_stacks.append(x)

original_crate_stacks[0] = ['B', 'S', 'V', 'Z', 'G', 'P', 'W']
original_crate_stacks[1] = ['J', 'V', 'B', 'C', 'Z', 'F']
original_crate_stacks[2] = ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C']
original_crate_stacks[3] = ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B']
original_crate_stacks[4] = ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H']
original_crate_stacks[5] = ['G', 'F', 'Q', 'T', 'S', 'L', 'B']
original_crate_stacks[6] = ['L', 'G', 'C', 'Z', 'V']
original_crate_stacks[7] = ['N', 'L', 'G']
original_crate_stacks[8] = ['J', 'F', 'H', 'C']
crate_stacks = copy.deepcopy(original_crate_stacks)

part1(crate_stacks, top_crates)
crate_stacks = copy.deepcopy(original_crate_stacks)

part2(crate_stacks, top_crates)