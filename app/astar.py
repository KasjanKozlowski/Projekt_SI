from heapq import heappush, heappop


DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def reconstruct_path(came_from, current):
    path = []

    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def astar(maze, start, end, heuristic):
    open_set = []
    heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}

    visited_nodes = 0

    while open_set:
        _, current = heappop(open_set)

        visited_nodes += 1

        if current == end:
            return reconstruct_path(came_from, current), visited_nodes

        for dx, dy in DIRECTIONS:
            nx = current[0] + dx
            ny = current[1] + dy

            neighbor = (nx, ny)

            if maze[nx][ny] == '#':
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor, end)

                heappush(open_set, (f_score, neighbor))

    return None, visited_nodes
