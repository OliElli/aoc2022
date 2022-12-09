#!/usr/bin/env python3

# Read input into tress list
with open("input_test.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]


def x_move():
    global h_coords
    global t_coords
    if h_coords[0] > t_coords[0]:
        print(f'move x 1')
        t_coords = (t_coords[0]+1,t_coords[1])
    else:
        print(f'move x -1')
        t_coords = (t_coords[0]-1,t_coords[1])


def y_move():
    global h_coords
    global t_coords
    if h_coords[1] > t_coords[1]:
        print(f'move y 1')
        t_coords = (t_coords[0],t_coords[1]+1)
    else:
        print(f'move y -1')
        t_coords = (t_coords[0],t_coords[1]-1)


def move(x, y):
    global h_coords
    global t_coords
    h_coords = (h_coords[0] + x, h_coords[1] + y)
    print('before',h_coords, t_coords)
    print(abs(h_coords[0] - t_coords[0]), abs(h_coords[1] - t_coords[1]))
    if abs(h_coords[0] - t_coords[0]) > 1 or abs(h_coords[1] - t_coords[1]) > 1:
    # elif t_coords[0] != h_coords[0] and t_coords[1] != h_coords[1]:
        x_move()
        y_move()
    elif t_coords[0] not in [h_coords[0]-1, h_coords[0], h_coords[0]+1]:
        x_move()
    elif t_coords[1] not in [h_coords[1]-1, h_coords[1], h_coords[1]+1]:
        y_move()
    trail[t_coords[0]][t_coords[1]] += 1
    # print(t_coords)
    print('after',h_coords, t_coords)
    print()


h_coords = (0,0)
t_coords = (0,0)

trail = []
for i in range(0, 10):
    trail.append([])
    for j in range(0, 10):
        trail[i].append(0)

for line in lines:
    direction, distance = line.split(' ')
    distance = int(distance)

    for i in range(0, distance):
        if direction == 'R':
            move(1,0)
        elif direction == 'L':
            move(-1,0)
        elif direction == 'U':
            move(0,1)
        elif direction == 'D':
            move(0,-1)

for x in trail:
    print(x)
print()
pt1 = 0
for x in trail:
    for y in trail[0]:
        if x[y] > 0:
            pt1 += 1

print(f'Pt1: {pt1}')
'''
(4, 0)
(4, 4)
(1, 4)
(1, 3)
(5, 3)
(5, 2)
(0, 2)
(2, 2)
'''
