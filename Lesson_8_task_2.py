# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

import random


def graph_create(n):
    """Функция создания списка смежности графа."""
    return {i: [0 if j == i else random.randint(0, n + 3) for j in range(n)] for i in range(n)}


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False for _ in range(length)]
    cost = [float('inf')] * length
    parent = {}

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, parent


n = 6
# g = graph_create(n)
g = {0: [0, 9, 0, 5, 3, 2],
     1: [7, 0, 3, 5, 9, 6],
     2: [6, 3, 0, 6, 7, 6],
     3: [6, 7, 9, 0, 7, 7],
     4: [1, 1, 4, 1, 0, 6],
     5: [3, 0, 6, 0, 0, 0]}

s = int(input('От какой вершины идти: '))
print(*g.items(), sep='\n')
print(dijkstra(g, s))