# Advent Of Code 2022 - Day 2

# Opening input file
fd = open("input.txt", "r")
lines = fd.readlines()
fd.close()

# =========================== PART 1 =========================== #
# Defining some functions 
def is_win(line):
    if line[0] == 'A':
        if line[2] == 'Y':
            return True
    
    if line[0] == 'B':
        if line[2] == 'Z':
            return True

    if line[0] == 'C':
        if line[2] == 'X':
            return True

    return False

def is_draw(line):
    if line[0] == 'A':
        if line[2] == 'X':
            return True

    if line[0] == 'B':
        if line[2] == 'Y':
            return True

    if line[0] == 'C':
        if line[2] == 'Z':
            return True

    return False

def is_loss(line):
    if line[0] == 'A':
        if line[2] == 'Z':
            return True
    
    if line[0] == 'B':
        if line[2] == 'X':
            return True

    if line[0] == 'C':
        if line[2] == 'Y':
            return True

    return False

pts = 0
# Dictionary with the shapes value
shapes_score = {'X' : 1, 'Y' : 2, 'Z' : 3}




for line in lines:
    if is_win(line):
        pts += shapes_score[line[2]] + 6
    elif is_draw(line):
        pts += shapes_score[line[2]] + 3
    else:
        pts += shapes_score[line[2]]

print(f"Your total score is: {pts}")

# =========================== PART 2 =========================== #
shapes = {'A' : 1, 'B' : 2, 'C' : 3}
winning = {'A': 'B', 'B' : 'C', 'C' : 'A'}
loosing = {'A': 'C', 'B' : 'A', 'C' : 'B'}

def right_calculation(line):
    # Loose
    if line[2] == 'X':
        return shapes[loosing[line[0]]]
    # Draw
    elif line[2] == 'Y':
        return shapes[line[0]] + 3
    # Win
    else:
        return shapes[winning[line[0]]] + 6

pts = 0
for line in lines:
    pts += right_calculation(line)

print(f"The right score is: {pts}")
