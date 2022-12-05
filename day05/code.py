#!/usr/bin/env python3

import re

def has_numbers(i):
    return any(char.isdigit() for char in i)

def move_crate(stack, src, dst):
    stack[dst].insert(0,stack[src].pop(0))
    return stack

def move_crate_pt2(stack2, src, dst, num):
    stack2[dst].insert(0,stack2[src][:num])
    stack2[src] = stack2[src][num:]
    stack2[dst] = [item for sublist in stack2[dst] for item in sublist]
    return stack2

# Read input
with open("input.txt") as f:
    stacks_block, gap, moves_block = f.read().partition("\n\n")

# Split stacks into lists
count = 0
stack_count = 0
stack = {}
stack2 = {}
# Create stack lists
for i in [stacks_block[i:i+4] for i in range(0, len(stacks_block), 4)]:
    if has_numbers(i):
        stack[stack_count] = []
        stack2[stack_count] = []
        stack_count += 1
# Fill in stacks
for i in [stacks_block[i:i+4] for i in range(0, len(stacks_block), 4)]:
    if '[' in i:
        crate = re.split(r'\[|\]', i)[1]
        stack[count].append(crate)
        stack2[count].append(crate)
    count += 1
    # Finally reset counter on newline
    if '\n' in i:
        count = 0

# Run the moves
moves_block = moves_block.strip()
move_list = moves_block.split('\n')
for move in move_list:
    moves = move.split(' ')
    num = int(moves[1])
    src = int(moves[3]) - 1
    dst = int(moves[5]) - 1
    # pt1
    for i in range(0, num):
        stack = move_crate(stack, src, dst)
    # pt2
    stack2 = move_crate_pt2(stack2, src, dst, num)

# Assemble the tops of each stack
pt1 = ''
pt2 = ''
for i in stack:
    pt1 = pt1 + stack[i].pop(0)
    pt2 = pt2 + stack2[i].pop(0)

print(f'Pt1 {pt1}')
print(f'Pt2 {pt2}')
