# Advent of Code - day 3

# Opening input.txt reading it and close the file.
fd = open("input.txt", "r")
lines = fd.readlines()
fd.close()

# Defining and initializing a dictionary for the priority
priority = dict()
lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = ""
for i in range(len(lowercase_alphabet)):
    uppercase_alphabet += lowercase_alphabet[i].capitalize()

alph = lowercase_alphabet + uppercase_alphabet
for i in range(1,53):
    priority[alph[i - 1]] = i

# PART 1
res = 0
flag = 0
c = ''
for line in lines:
    p = len(line)//2
    fst_half = line[:p] 
    snd_half = line[p:]
    for i in range(p):
        for k in range(p):
            if fst_half[i] == snd_half[k]:
                if fst_half[i] != flag:
                    res += priority[fst_half[i]]
                    flag = fst_half[i]
                    print(f"i: {i}, 1st: {fst_half[i]}; k: {k}, 2nd: {snd_half[k]};  priority: {priority[fst_half[i]]}; 1st Half: {fst_half}; 2nd Half: {snd_half}")

    
print(f"Priority: {res}")

# PART 2
def find_in(row, c):
    for t in row:
        if c == t:
            return True

    return False

def badge(elf1, elf2, elf3):
    for c in elf1:
            for r in elf2:
                if c == r:
                    if find_in(elf3, c):
                        return c
badge_sum = 0

for i in range(0,len(lines),3):
    row1 = lines[i]
    row2 = lines[i+1]
    row3 = lines[i+2]

    tmp = badge(row1, row2, row3)
    badge_sum += priority[tmp]
    
    print(f"Elf group #: {i} | Badge: {tmp} | Badge priority: {priority[tmp]}")

print(f"Badge priority sum: {badge_sum}")
        
    

    





        
