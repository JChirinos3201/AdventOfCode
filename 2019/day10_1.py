import pprint
import math
import time
import numpy as np

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

def go():
    t = time.time()
    s = open('day10_INPUT.txt').read().strip()
##    s = '''.#..#
##.....
#######
##....#
##...##'''
##    s = '''......#.#.
###..#.#....
##..#######.
##.#.#.###..
##.#..#.....
##..#....#.#
###..#....#.
##.##.#..###
####...#..#.
##.#....####'''

    coords = [list(i) for i in s.split('\n')]

    print(calculate(coords))

    
    
    print(time.time() - t)
