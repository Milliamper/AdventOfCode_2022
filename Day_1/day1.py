def sumCalories():
    my_array = []
    maxSum = 0
    sum = 0

    input = open(
        "/Users/mrtn/Documents/AdventOfCalendar_2022/Day_1/input.txt", "r")

    for line in input.readlines():
        if (line[0] != '\n'):
            sum += int(line)
        else:
            my_array.append(sum)
            sum = 0
            continue

    my_array.sort()

    arrayToBeSum = my_array[-3:]

    finalSum = 0
    for i in range(0, len(arrayToBeSum)):
        finalSum += arrayToBeSum[i]
    
    print(finalSum)


sumCalories()

