class Node:

    def __init__(self, val, parent):
        self.val = val
        self.children = []
        self.parent = parent

# relations is dict
def get_to_santa(relations):
    root = Node('COM', None)
    nodes = []
    populate(root, relations, nodes)
    goal = None
    node_at = None
    for node in nodes:
        if node.val == 'SAN':
            goal = node.parent
        elif node.val == 'YOU':
            node_at = node
        if goal and node_at:
            break
    moves = 0
    while not search_in_children(node_at, goal):
        node_at = node_at.parent
        moves += 1
    while node_at != goal:
        for child in node_at.children:
            if search_in_children(child, goal):
                node_at = child
                moves += 1
                break
    return moves
    

def populate(node, relations, nodes):
    nodes.append(node)
    if node.val not in relations:
        return
    node.children = [Node(i, node) for i in relations.get(node.val)]
    for child in node.children:
        populate(child, relations, nodes)

def search_in_children(node, goal):
    if node == goal:
        return True
    for n in node.children:
        if search_in_children(n, goal):
            return True
    return False

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
    return get_to_santa(d)
