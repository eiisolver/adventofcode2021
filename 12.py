class Node(object):
    def __init__(self, name) -> None:
        self.name = name
        self.is_small = name.islower()
        self.is_start = name == 'start'
        self.is_end = name == 'end'
        self.neighbours = set()
        self.visits = 0
    
    def add(self, n):
        self.neighbours.add(n)
        n.neighbours.add(self)

def nr_paths(nodes, multi_visit_allowed, node_predicate):
    paths = 0

    def visit(n, multi_visit_allowed):
        nonlocal paths
        if n.is_end:
            paths += 1
        else:
            n.visits += 1
            for n2 in n.neighbours:
                multi_visit = n2.is_small and n2.visits >= 1
                if node_predicate(n2) and (multi_visit_allowed or not multi_visit):
                    visit(n2, multi_visit_allowed and not multi_visit)
            n.visits -= 1
    
    visit(nodes['start'], multi_visit_allowed)
    print('Number of paths:', paths)

lines = open('12_input.txt', 'r').read().splitlines()
edges = [ line.split('-') for line in lines ]
nodes = { name: Node(name) for edge in edges for name in edge }
for edge in edges:
    nodes[edge[0]].add(nodes[edge[1]])

nr_paths(nodes, False, lambda n: n.visits == 0 or not n.is_small)
nr_paths(nodes, True, lambda n: n.visits == 0 or not n.is_small or (n.visits == 1 and not n.is_start))
