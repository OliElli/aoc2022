#!/usr/bin/env python3

# Read input
with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]

pt1 = 0
pt2 = 0

for line in lines:
    x,y = line.split(',')
    x_lower,x_upper = x.split('-')
    y_lower,y_upper = y.split('-')

    x_range = range(int(x_lower),int(x_upper)+1)
    y_range = range(int(y_lower),int(y_upper)+1)
    intersection = set(x_range).intersection(y_range)

    if intersection == set(x_range) or intersection == set(y_range):
        pt1 = pt1 + 1
    if intersection:
        pt2 = pt2 + 1

print(f'Pt1 {pt1}')
print(f'Pt2 {pt2}')
