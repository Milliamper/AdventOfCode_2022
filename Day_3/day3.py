filename = "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_3/input.txt"


def rucksack_reorganization(filename):

    lines = []
    list_of_words = []
    first_half = []
    second_half = []
    sum_of_values = 0

    my_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,

        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    for i in range(0, len(lines)):
        list_of_words = list(lines[i])

        first_half = list_of_words[:len(list_of_words)//2]
        second_half = list_of_words[len(list_of_words)//2:]

        same_element = list(set(first_half).intersection(second_half))

        sum_of_values += my_dict[same_element[0]]

    print(sum_of_values)


def rucksack_reorganization_part2(filename):

    lines = []
    sum_of_values = 0

    my_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,

        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    for i in range(0, len(lines), 3):
        same_element = list(set(lines[i]).intersection(
            lines[i + 1]).intersection(lines[i + 2]))
        sum_of_values += my_dict[same_element[0]]
        same_element.clear()

    print(sum_of_values)


rucksack_reorganization(filename)
rucksack_reorganization_part2(filename)
