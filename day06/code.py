#!/usr/bin/env python3

# Read input
with open("input.txt") as f:
    lines = f.readlines()

chars1 = ""
chars2 = ""
count = 1
for char in lines[0]:
    chars1 += char
    chars2 += char
    if len(chars1) == 4:
        if len(set(chars1)) == len(chars1):
            print(f"Pt1: {count}")
        else:
            chars1 = chars1[1:]
    if len(chars2) == 14:
        if len(set(chars2)) == len(chars2):
            print(f"Pt1: {count}")
        else:
            chars2 = chars2[1:]
    count += 1
