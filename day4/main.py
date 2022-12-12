# Advent of Code 2022 - Day 4

# Opening input file and divide the elves pairs in two 
# separated lists
with open("input.txt", "r") as fd:
    lines = fd.readlines()
    assignement_pairs = [entry.strip() for entry in lines]

# =========================== PART 1 =========================== #
def is_range_contained(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    return start_b <= start_a and end_a <= end_b 

pairs_contained = 0
for assignement_pair in assignement_pairs:
    first_range, second_range = assignement_pair.split(',')
    if is_range_contained(first_range, second_range) or is_range_contained(second_range, first_range):
        pairs_contained += 1

print(f"Part 1 pairs: {pairs_contained}")

# =========================== PART 2 =========================== #
def is_partial_range_contained(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    start_contained = start_b <= start_a and start_a <= end_b 
    end_contained = start_b <= end_a and end_a <= end_b
    return start_contained or end_contained 

partial_pairs = 0
for assignement_pair in assignement_pairs:
    first_range, second_range = assignement_pair.split(',')
    if is_partial_range_contained(first_range, second_range) or is_partial_range_contained(second_range, first_range):
        partial_pairs += 1

print(f"Part 2 pairs: {partial_pairs}")