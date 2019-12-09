def make_point_list(inst):
    # makes a dict: key=(x, y), val=steps_taken
    # if point is revisited, doesn't update
    pts = dict()

    inst_list = inst.split(',')

    x, y = 0, 0
    s = 0

    for i in inst_list:
        if i[0] == 'R':
            for _ in range(int(i[1:])):
                x += 1
                s += 1
                if (x, y) not in pts:
                    pts[(x, y)] = s
        elif i[0] == 'L':
            for _ in range(int(i[1:])):
                x -= 1
                s += 1
                if (x, y) not in pts:
                    pts[(x, y)] = s
        elif i[0] == 'U':
            for _ in range(int(i[1:])):
                y += 1
                s += 1
                if (x, y) not in pts:
                    pts[(x, y)] = s
        elif i[0] == 'D':
            for _ in range(int(i[1:])):
                y -= 1
                s += 1
                if (x, y) not in pts:
                    pts[(x, y)] = s
    return pts

def get_fewest_steps(one, two):
    min_steps = None
    for o_pt in one:
        if o_pt in two:
            if (not min_steps) or one[o_pt] + two[o_pt] < min_steps:
                min_steps = one[o_pt] + two[o_pt]
    return min_steps

def go():
    s = open('day3_INPUT.txt').read()
    one_raw, two_raw = s.split()
    one = make_point_list(one_raw)
    two = make_point_list(two_raw)
    print(get_fewest_steps(one, two))
