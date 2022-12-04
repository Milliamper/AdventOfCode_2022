import numpy as np

filename = "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_4/input.txt"


def camp_cleanup(filename):

    lines = []
    elements = []

    pair_one = []
    pair_two = []

    count = 0

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip().split(","))

    for i in range(0, len(lines)):
        for j in range(0, 2):
            for k in range(0, 2):
                elements.append(lines[i][j].split('-')[k])

        pair_one = list(
            range(int(lines[i][0].split("-")[0]), int(lines[i][0].split("-")[1])+1))
        pair_two = list(
            range(int(lines[i][1].split("-")[0]), int(lines[i][1].split("-")[1])+1))

        print("i: ", i)
        print("one: ", pair_one)
        print("two: ", pair_two)

        ans3 = list(set(pair_one) & set(pair_two))
        print(ans3.sort())

        if (ans3 == pair_one or ans3 == pair_two):
            count += 1

    print("Count: ", count)


def camp_cleanup_part2(filename):

    lines = []
    elements = []

    pair_one = []
    pair_two = []

    count = 0

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip().split(","))

    for i in range(0, len(lines)):
        for j in range(0, 2):
            for k in range(0, 2):
                elements.append(lines[i][j].split('-')[k])

        pair_one = list(
            range(int(lines[i][0].split("-")[0]), int(lines[i][0].split("-")[1])+1))
        pair_two = list(
            range(int(lines[i][1].split("-")[0]), int(lines[i][1].split("-")[1])+1))

        print("i: ", i)
        print("one: ", pair_one)
        print("two: ", pair_two)

        ans3 = list(set(pair_one) & set(pair_two))
        print(ans3.sort())

        if any(x in pair_one for x in pair_two):
            count += 1

    print("Count: ", count)


# camp_cleanup(filename)
camp_cleanup_part2(filename)
