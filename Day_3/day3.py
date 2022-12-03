filename = "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_3/input.txt"


def rucksack_reorganization(filename):

    lines = []
    list_of_words = []
    first_half = []
    second_half = []
    value = 0
    sum_of_values = 0

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    for i in range(0, 10):
        list_of_words = list(lines[i])

        first_half = list_of_words[:len(list_of_words)//2]
        second_half = list_of_words[len(list_of_words)//2:]

        same_element = list(set(first_half).intersection(second_half))

        if (same_element[0].islower):
            value = ord(same_element[0])-96
        else:
            value = ord(same_element[0])-38

        print("same: ", same_element[0])
        print("value: ", value)
        sum_of_values += value
        value = 0
        first_half.clear()
        second_half.clear()
        same_element.clear()

    print(sum_of_values)


rucksack_reorganization(filename)
