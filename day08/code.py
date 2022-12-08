#!/usr/bin/env python3

# Read input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

trees = []
pt1 = 0

for line in lines:
    trees.append(list(line))


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
            if x == 2 and y == 3:
                # print('score: ', innerscore[x][y])
                pass
            if x == 1 and y == 1:
                # print('score: ', innerscore[x][y])
                # print(score1[x][y], score2[x][y], score3[x][y], score4[x][y])
                pass
    return innerscore


trees = trees
trees90 = rotate(trees, 1)
trees180 = rotate(trees, 2)
trees270 = rotate(trees, 3)

score = find_score(trees)
score90 = find_score(trees90)
score180 = find_score(trees180)
score270 = find_score(trees270)

score1 = score
score2 = rotate(score90, 3)
score3 = rotate(score180, 2)
score4 = rotate(score270, 1)

scorematrix = multi_score(score, score2, score3, score4)

pt2 = 0
for x, row in enumerate(scorematrix):
    for y, tree in enumerate(row):
        if scorematrix[x][y] > pt2:
            pt2 = scorematrix[x][y]
print(f'Pt2: {pt2}')
