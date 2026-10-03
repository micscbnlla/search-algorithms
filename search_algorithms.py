from collections import deque
import heapq

graph = {
    'S': ['A', 'C'],
    'A': ['S', 'G'],
    'C': ['S', 'D', 'E'],
    'D': ['C', 'G'],
    'E': ['C', 'G'],
    'G': ['A', 'D', 'E']
}


def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None


def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in reversed(graph[current]):
                new_path = path + [neighbor]
                stack.append(new_path)

    return None


weighted_graph = {
    'S': {'A': 5, 'C': 4},
    'A': {'S': 5, 'G': 4},
    'C': {'S': 4, 'D': 3, 'E': 2},
    'D': {'C': 3, 'G': 1},
    'E': {'C': 2, 'G': 8},
    'G': {'A': 4, 'D': 1, 'E': 8}
}


heuristic = {
    'S': 8,
    'A': 4,
    'C': 4,
    'D': 1,
    'E': 6,
    'G': 0
}


def astar(graph, heuristic, start, goal):
    priority_queue = []

    g_cost = 0
    f_cost = g_cost + heuristic[start]

    heapq.heappush(
        priority_queue,
        (f_cost, g_cost, start, [start])
    )

    visited = set()

    while priority_queue:
        f_cost, g_cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, g_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current].items():
            new_g_cost = g_cost + cost
            new_f_cost = new_g_cost + heuristic[neighbor]
            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_f_cost, new_g_cost, neighbor, new_path)
            )

    return None, None


start = 'S'
goal = 'G'


bfs_path = bfs(graph, start, goal)

print("BFS - Breadth First Search")
print("Start:", start)
print("Goal:", goal)
print("Path:", " -> ".join(bfs_path))


dfs_path = dfs(graph, start, goal)

print("\nDFS - Depth First Search")
print("Start:", start)
print("Goal:", goal)
print("Path:", " -> ".join(dfs_path))


astar_path, total_cost = astar(
    weighted_graph,
    heuristic,
    start,
    goal
)

print("\nA* Search")
print("Start:", start)
print("Goal:", goal)
print("Path:", " -> ".join(astar_path))
print("Total Cost:", total_cost)


print("\nSearch Complete")