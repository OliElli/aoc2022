#!/usr/bin/env python3

# Read guide
with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]

result = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
]
play = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}
result_pt2 = [
    ['C','A','B'],
    ['A','B','C'],
    ['B','C','A'],
]
ldw = [0,3,6]

guide = {}
total_score = 0
total_score_pt2 = 0
for line in lines:
    # pt1
    enemy, hero = line.split(' ')
    guide[enemy] = hero
    score = result[play[enemy]][play[hero]]
    total_score = total_score + score + play[hero] + 1

    # pt2
    total_score_pt2 = total_score_pt2 + play[result_pt2[play[enemy]][play[hero]]] + 1 + ldw[play[hero]]
print(f'Pt1 {total_score}')
print(f'Pt2 {total_score_pt2}')
