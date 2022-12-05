# Advent of Code 2022 - Day 4

# Opening input file
fd = open("input.txt", "r")
lines = fd.readlines()
fd.close()

# PART 1
pairs = 0
old_pairs = 0
for line in lines:
    old_pairs = pairs
    elf1_low = int(line.split('-')[0])
    elf1_high = int(line.split('-')[1].split(',')[0])
    elf2_low = int(line.split(',')[1].split('-')[0])
    elf2_high = int(line.split(',')[1].split('-')[1])

    if elf1_low <= elf2_low and elf1_high >= elf2_high:
        pairs += 1
        print(f"LOW: Elf1 = {elf1_low}; Elf2 = {elf2_low} | HIGH: Elf1 = {elf1_high}; Elf2 = {elf2_high} | Pairs: {pairs}")
    
    if elf2_low <= elf1_low and elf2_high >= elf1_high:
        #print(f"LOW: Elf1 = {elf1_low}; Elf2 = {elf2_low} | HIGH: Elf1 = {elf1_high}; Elf2 = {elf2_high} |  Pairs: {pairs}")
        pairs += 1
    
    #if old_pairs != pairs:
        #print(f"First elf: {elf1_low} to {elf1_high}; Second elf: {elf2_low} to {elf2_high}; Pairs: {pairs}")

print(f"Pairs: {pairs}")