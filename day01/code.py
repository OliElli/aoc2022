#!/usr/bin/env python3

# Read inputs
with open('input.txt') as f:
    lines = f.readlines()

elves = [0]
counter = 0
for line in lines:
    line = line.strip()
    if line == '':
        counter = counter + 1
        elves.append(0)
        continue
    else:
        line = int(line)
        elves[counter] = elves[counter] + line

# Find Elf with most calories
print(f'Pt1: {max(elves)}')

# Remove the top elf 3 times and sum the removed elves:
pt2 = 0
for i in range(3):
    pt2 = pt2 + max(elves)
    elves.remove(max(elves))

print(f'Pt2: {pt2}')
