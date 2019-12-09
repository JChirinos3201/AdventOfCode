def make_point_list(inst):
    pts = set()

    inst_list = inst.split(',')

    x, y = 0, 0

    for i in inst_list:
        if i[0] == 'R':
            for _ in range(int(i[1:])):
                x += 1
                pts.add((x, y))
        elif i[0] == 'L':
            for _ in range(int(i[1:])):
                x -= 1
                pts.add((x, y))
        elif i[0] == 'U':
            for _ in range(int(i[1:])):
                y += 1
                pts.add((x, y))
        elif i[0] == 'D':
            for _ in range(int(i[1:])):
                y -= 1
                pts.add((x, y))
    return pts

def get_closest(one, two):
    min_d = None
    for o_pt in one:
        if o_pt in two:
            if (not min_d) or sum(map(abs, o_pt)) < min_d:
                min_d = sum(map(abs,o_pt))
    return min_d

def go():
    s = open('day3_INPUT.txt').read()
    one_raw, two_raw = s.split()
    one = make_point_list(one_raw)
    two = make_point_list(two_raw)
    print(get_closest(one, two))
