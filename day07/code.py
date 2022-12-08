#!/usr/bin/env python3

import re

# Read input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

directory = []
filesizes = {}


def pt1():
    for line in lines:
        if line.startswith("$ cd"):
            if ".." in line:
                directory.pop(-1)
            else:
                directory.append(line.split("$ cd ")[1])
                if ''.join(directory) not in filesizes.keys():
                    filesizes.update({''.join(directory): 0})
            continue
        if (filesize := re.findall("\d+ ", line)) != []:
            update = []
            for dir in directory:
                update.append(dir)
                filesizes.update({''.join(update): filesizes.get(''.join(update))+int(filesize[0])})
    small_dirs = []
    for x,y in filesizes.items():
        if y <= 100000:
            small_dirs.append(filesizes.get(x))
    return (sum(small_dirs))


def pt2():
    minimumSpace = 30000000 - (70000000 - filesizes.get('/'))
    listPossible = []
    for values in filesizes.values():
        if values >= minimumSpace:
            listPossible.append(values)
    return (min(listPossible))


print(f'Pt1: {pt1()}')
print(f'Pt2: {pt2()}')
