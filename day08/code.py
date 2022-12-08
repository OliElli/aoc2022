#!/usr/bin/env python3

# Read input into tress list
trees = []
with open("input.txt") as f:
    lines = [trees.append(list(line.rstrip())) for line in f.readlines()]

def rotate(thing, times):
    for i in range(0,times):
        thing = list(zip(*reversed(thing)))
    for i, j in enumerate(thing):
        thing[i] = list(thing[i])
    return thing

def check_height(trees):
    count = 0
    visible = []
    for row in trees:
        max = 0
        visible.append([])
        for i, tree in enumerate(row):
            if int(tree) > max or i == 0:
                max = int(tree)
                visible[count].append(1)
            else:
                visible[count].append(0)
        count += 1
    return visible

visible = check_height(trees)
visible90 = check_height(rotate(trees, 1))
visible180 = check_height(rotate(trees, 2))
visible270 = check_height(rotate(trees, 3))

score = []
vis = [x for l in visible for x in l]
vis90 = [x for l in rotate(visible90, 3) for x in l]
vis180 = [x for l in rotate(visible180, 2) for x in l]
vis270 = [x for l in rotate(visible270, 1) for x in l]

pt1 = 0
for i, item in enumerate(vis):
    score = vis[i] + vis90[i] + vis180[i] + vis270[i]
    if score > 0:
        pt1 += 1

print(f'Pt1: {pt1}')

score = []
for x, row in enumerate(trees):
    score.append([])
    for y, tree in enumerate(row):
        score[x].append(0)

def find_score(trees):
    score = []
    for x, row in enumerate(trees):
        score.append([])
        for y, tree in enumerate(row):
            score[x].append(0)
        for y, tree in enumerate(row):
            for i in range (y+1, len(score[x])):
                if int(tree) <= int(row[i]):
                    score[x][y] += 1
                    break
                else:
                    score[x][y] += 1
    return score

def multi_score(score1, score2, score3, score4):
    innerscore = []
    for x, row in enumerate(score1):
        innerscore.append([])
        for y, tree in enumerate(row):
            innerscore[x].append(0)
        for y, tree in enumerate(row):
            innerscore[x][y] = score1[x][y] * score2[x][y] * score3[x][y] * score4[x][y]
    return innerscore

scorematrix = multi_score(
    find_score(trees),
    rotate(find_score(rotate(trees, 1)), 3),
    rotate(find_score(rotate(trees, 2)), 2),
    rotate(find_score(rotate(trees, 3)), 1)
)

pt2 = 0
for x, row in enumerate(scorematrix):
    for y, tree in enumerate(row):
        if scorematrix[x][y] > pt2:
            pt2 = scorematrix[x][y]
print(f'Pt2: {pt2}')
