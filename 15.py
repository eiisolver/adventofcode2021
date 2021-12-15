import heapq
import numpy as np

class Node(object):
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.neighbours = set()

    def add(self, n):
        self.neighbours.add(n)
        n.neighbours.add(self)

def dijkstra(graph, start_node):
    distance = len(graph) * [1e9]
    distance[start_node] = 0
    queue = [(0, start_node)]
    while len(queue) > 0:
        curr_dist, v = heapq.heappop(queue)
        if curr_dist > distance[v]:
            continue
        for n2 in graph[v].neighbours:
            w = n2.id
            dist_v = curr_dist + n2.value
            if dist_v < distance[w]:
                distance[w] = dist_v
                heapq.heappush(queue, (dist_v, w))
    return distance

def find_shortest_path(risk_level):
    h = len(risk_level)
    w = len(risk_level[0])
    graph = [Node(y * w + x, risk_level[y][x]) for y in range(h) for x in range(w)]
    for x in range(w):
        for y in range(h):
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + a < w and 0 <= y + b < h:
                    graph[w * y + x].add(graph[w * (y + b) + x + a])
    distance = dijkstra(graph, 0)
    print('Total risk:', distance[len(graph)-1])

def extend(matrix, axis):
    result = np.copy(matrix)
    prev = result
    for _ in range(4):
        m = np.copy(prev)
        m += 1
        m = np.where(m == 10, 1, m)
        prev = m
        result = np.concatenate((result, m), axis=axis)
    return result

arr = []
for line in open('15_input.txt', 'r').read().splitlines():
    arr.append([int(c) for c in line])
risk_level1 = np.asarray(arr, np.int8)
find_shortest_path(risk_level1)
risk_level2 = extend(risk_level1, 1)
risk_level2 = extend(risk_level2, 0)
find_shortest_path(risk_level2)
