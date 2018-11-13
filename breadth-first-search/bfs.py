class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs(node, searching_for):
    unvisited = []
    visited = []

    unvisited.append(node)

    while unvisited != []:
        curr_node = unvisited.pop(0) # remove and return item 0
        print(curr_node.value)

        if curr_node.value == searching_for:
            return curr_node

        for child in curr_node.children:
            if child in visited:
                continue

            if child not in unvisited:
                unvisited.append(child)

        visited.append(curr_node)

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
a.children.append(b)
a.children.append(c)
b.children.append(d)
b.children.append(e)
c.children.append(f)
c.children.append(g)
e.children.append(h)

result = bfs(a, "H")
print(result)
print(result.value)

'''
                 A
               /   \
              B      C
             / \    / \
            D   E  F    G
                |
                H
'''