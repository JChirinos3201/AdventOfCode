class Node:

    def __init__(self, val, parent):
        self.val = val
        self.children = []
        self.parent = parent

# relations is dict
def count_orbits(relations):
    root = Node('COM', None)
    nodes = []
    populate(root, relations, nodes)
    count = 0
    for node in nodes:
        count += count_relatives(node)
    return count

def populate(node, relations, nodes):
    nodes.append(node)
    if node.val not in relations:
        return
    node.children = [Node(i, node) for i in relations.get(node.val)]
    for child in node.children:
        populate(child, relations, nodes)

def count_relatives(node):
    if node.parent == None:
        return 0
    return 1 + count_relatives(node.parent)

def go():
    s = open('day6_INPUT.txt').read()
    l = s.split('\n')
    d = {}
    for i in l[:-1]:
        orbited, orbiting = i.split(')')
        if orbited in d:
            d[orbited].append(orbiting)
        else:
            d[orbited] = [orbiting]
    return count_orbits(d)
