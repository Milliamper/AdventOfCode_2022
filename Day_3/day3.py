filename = "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_3/input.txt"

def rucksack_reorganization(filename):

    lines = []
    first_half = []
    second_half = []

    

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    first_half_slicer = slice(int(len(lines)/2))
    
    for i in range(0, 1):
        for letter in lines[i]:
            #print(len(lines[i]))
            print(len(lines[first_half_slicer]))


rucksack_reorganization(filename)