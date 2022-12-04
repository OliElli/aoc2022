#!/usr/bin/env python3

# Read input
with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]

def get_priority(item):
    # Assign priority value to duplicate item
    if item.isupper():
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    return priority

pt1 = 0
pt2 = 0
group_counter = 0
group = {}
for line in lines:
    # Find the item that appears in both compartments
    compart1 = line[slice(0,len(line)//2)]
    compart2 = line[slice(len(line)//2, len(line))]
    item = set(compart1).intersection(compart2).pop()

    # Sum the values
    pt1 = pt1 + get_priority(item)

    # Pt2


    group[group_counter] = line
    if group_counter == 2:
        badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        pt2 = pt2 + get_priority(badge)
        group_counter = 0
    else:
        group_counter = group_counter + 1


print(f'Pt1 {pt1}')
print(f'Pt2 {pt2}')
