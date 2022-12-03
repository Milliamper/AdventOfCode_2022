filename = "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_2/input.txt"

def Rock_Paper_Scissors(filename):

    X = 1  # rock
    Y = 2  # paper
    Z = 3  # scissors
    lose = 0
    draw = 3
    win = 6
    lines = []

    total_points = 0
    game_point = 0

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    # game cases
    loss_cases = ['A Z', 'B X', 'C Y']
    draw_cases = ['A X', 'B Y', 'C Z']
    win_cases = ['A Y', 'B Z', 'C X']

    for i in range(0, len(lines)):
        if ("X" in lines[i]):
            game_point += X
        elif ("Y" in lines[i]):
            game_point += Y
        else:
            game_point += Z

        total_points += game_point
        game_point = 0

        if (lines[i] == draw_cases[0] or lines[i] == draw_cases[1] or lines[i] == draw_cases[2]):
            total_points += draw
        elif (lines[i] == win_cases[0] or lines[i] == win_cases[1] or lines[i] == win_cases[2]):
            total_points += win
        else:
            total_points += lose

    print(total_points)


def Rock_Paper_Scissors_Part2(filename):
    X = 1  # rock
    Y = 2  # paper
    Z = 3  # scissors
    lose = 0
    draw = 3
    win = 6
    lines = []

    total_points = 0
    game_point = 0

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    for i in range(0, len(lines)):
        if ("X" in lines[i]):
            total_points += lose
        elif ("Y" in lines[i]):
            total_points += draw
        else:
            total_points += win

        if ('A' in lines[i] and 'X' in lines[i]):
            total_points += Z
        elif ('A' in lines[i] and 'Y' in lines[i]):
            total_points += X
        elif ('A' in lines[i] and 'Z' in lines[i]):
            total_points += Y

        elif ('B' in lines[i] and 'X' in lines[i]):
            total_points += X
        elif ('B' in lines[i] and 'Y' in lines[i]):
            total_points += Y
        elif ('B' in lines[i] and lines[i].find('Z')):
            total_points += Z

        elif ('C' in lines[i] and 'X' in lines[i]):
            total_points += Y
        elif ('C' in lines[i] and 'Y' in lines[i]):
            total_points += Z
        elif ('C' in lines[i] and 'Z' in lines[i]):
            total_points += X

    print(total_points)

Rock_Paper_Scissors(filename)
Rock_Paper_Scissors_Part2(filename)
