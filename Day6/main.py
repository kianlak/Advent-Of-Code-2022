import sys
sys.dont_write_bytecode = True # Removes pycache from generating
from Day6Part1 import *
from Day6Part2 import *

datastream_buffer = ""
with open('datastream_buffer.txt') as file:
    datastream_buffer = file.readline()

part1(datastream_buffer)
part2(datastream_buffer)