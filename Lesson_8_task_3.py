# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_create(n):
    """Функция создания списка смежности невзвешенного графа."""
    return {i: {j for j in range(random.randint(1, n), random.randint(2, n + 1)) if j != i} for i in range(1, n + 1)}


def dfs(graph, vertex, visited):
    """Функция обхода в глубину."""
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# num = int(input('Enter the deep of graph: '))
num = 6
g = graph_create(num)

"""
Подсчет количества компонент связанности.
"""
visited = set()
num_components = 0
for v in g:
    if v not in visited:
        dfs(g, v, visited)
        num_components += 1


print(*g.items(), sep='\n')
print(f'Количество компонент связанности: {num_components}')
print(visited)
