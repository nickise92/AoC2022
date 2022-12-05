# Advent O f Code 2022 - Day 1

# Opening input file
fd = open("input.txt", "r")
lines = fd.readlines()
fd.close()

# PART 1
# Defining function to find max value from input file
def find_max(lines):
    value = 0
    max_value = 0

    for line in lines:
        if line == '\n':
            if max_value < value:
                max_value = value

            value = 0
            continue                  # jump to next iteration

        else:
            value += int(line)       # turn str into int and add up
        
    return max_value

first = find_max(lines)
print(f"Result part 1: {first}")

# PART 2
def find_next(lines, ctrl_value):
    next_max = 0
    value = 0

    for line in lines:
        if line == '\n':
            if next_max < value and value < ctrl_value:
                next_max = value

            value = 0
            continue                  # jump to next iteration

        else:
            value += int(line)       # turn str into int and add up
        
    return next_max

second = find_next(lines, first)
third = find_next(lines, second)
print(f"First: {first}; \nSecond: {second}; \nThird: {third}")

sum = first + second + third;

print(f"Result part 2: {sum}") 