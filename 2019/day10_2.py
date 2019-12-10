# NOTE:
# This is definitely not exemplary work
# This highkey shouldn't even work
# It didn't really work for the test case
# But it did give me the right answer for my input
# And in the end, isn't that what really matters? ;3

import pprint
import math
import time

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def is_blocked(station, asteroid_A, asteroid_B):
    # if distance to a > distance to b: ignore case
    if dist(station, asteroid_A) > dist(station, asteroid_B):
        return False
    try:
##        station_A_ratio = (asteroid_A[0] - station[0]) / (asteroid_A[1] - station[1])
        station_A_ratio = math.atan2(asteroid_A[1] - station[1], asteroid_A[0] - station[0])
    except ZeroDivisionError:
        if asteroid_A[1] > station[1]:
            station_A_ratio = '+inf'
        else:
            station_A_ratio = '-inf'
    try:
##        station_B_ratio = (asteroid_B[0] - station[0]) / (asteroid_B[1] - station[1])
        station_B_ratio = math.atan2(asteroid_B[1] - station[1], asteroid_B[0] - station[0])
    except ZeroDivisionError:
        if asteroid_B[1] > station[1]:
            station_B_ratio = '+inf'
        else:
            station_B_ratio = '-inf'
##    print(station_A_ratio)
##    print(station_B_ratio)
    return station_A_ratio == station_B_ratio

def calculate(coords):
    visibility_arr = [[0] * len(coords[0]) for i in coords]
    asteroid_coords = []
    for x in range(len(coords)):
        for y in range(len(coords[x])):
            if coords[x][y] == '#':
                asteroid_coords.append( (x, y) )

    for station in asteroid_coords:
        visible = {}
        for a in asteroid_coords:
            visible[a] = True
        for asteroid_A in asteroid_coords:
            for asteroid_B in asteroid_coords:
                if station == asteroid_B:
                    visible[asteroid_B] = False
                if asteroid_A == station or asteroid_A == asteroid_B or asteroid_B == station:
                    continue
                if visible[asteroid_B]:
                    if is_blocked(station, asteroid_A, asteroid_B):
                        visible[asteroid_B] = False
        visibility_arr[station[0]][station[1]] = list(visible.values()).count(True)

    largest = 0
    c = (0, 0)
    for x in range(len(visibility_arr)):
        for y in range(len(visibility_arr[x])):
            if visibility_arr[x][y] > largest:
                largest = visibility_arr[x][y]
                c = (x, y)

    return largest, c, asteroid_coords

def vaporize(start, asteroid_coords):

    def asteroid_sort(a):
        nonlocal start
        return (a[0], math.sqrt(math.pow(start[0] - a[1][0], 2) + math.pow(start[1] - a[1][1], 2)))
    
    count = 0
    angles = []
    for i in asteroid_coords:
        if i == start:
            continue
        if i[0] - start[0] >= 0:
            angle = math.atan2(i[0] - start[0], i[1] - start[1])
            if angle >= (3 * math.pi) / 2:
                angle -= (2 * math.pi)
            angles.append((angle, i))
        else:
            angle = math.atan2(i[0] - start[0], i[1] - start[1]) + 2 * math.pi
            if (angle >= (3 * math.pi) / 2):
                angle -= (2 * math.pi)
            angles.append((angle, i))
    angles = sorted(angles, key=asteroid_sort)
    last_angle = 40000
    existing_asteroids = {}
    kilt = None
    for i in asteroid_coords:
        existing_asteroids[i] = True
    i = 0
    try:
        while count < 200:
            if existing_asteroids[angles[i][1]] and last_angle != angles[i][0]:
                existing_asteroids[angles[i][1]] = False
                last_angle = angles[i][0]
                count += 1
                kilt = angles[i]
                print(angles[i])
            i += 1
            i %= len(angles)
    except:
        print(i)
        print(angles)
    return kilt

def go():
    t = time.time()
    s = open('day10_INPUT.txt').read().strip()
##    s = '''.#..##.###...#######
####.############..##.
##.#.######.########.#
##.###.#######.####.#.
#######.##.#.##.###.##
##..#####..#.#########
######################
###.####....###.#.#.##
####.#################
#######.##.###..####..
##..######..##.#######
######.##.####...##..#
##.#####..#.######.###
####...#.##########...
###.##########.#######
##.####.#.###.###.#.##
##....##.##.###..#####
##.#.#.###########.###
###.#.#.#####.####.###
#####.##.####.##.#..##'''

    coords = [list(i) for i in s.split('\n')]

    largest, start, asteroid_coords = calculate(coords)

##    print(largest, start, asteroid_coords)
    print(start)

    print(vaporize(start, asteroid_coords))
    
    print(time.time() - t)
