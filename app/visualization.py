import matplotlib.pyplot as plt


COLOR_MAP = {
    '#': 0,
    '.': 1,
    'S': 2,
    'E': 3,
    '*': 4,
}



def print_maze(maze, path):
    maze_copy = [row[:] for row in maze]

    for x, y in path:
        if maze_copy[x][y] not in ['S', 'E']:
            maze_copy[x][y] = '*'

    print()

    for row in maze_copy:
        print(''.join(row))



def visualize(maze, path, title="Maze"):
    maze_copy = [row[:] for row in maze]

    for x, y in path:
        if maze_copy[x][y] not in ['S', 'E']:
            maze_copy[x][y] = '*'

    numeric_maze = []

    for row in maze_copy:
        numeric_row = []

        for cell in row:
            numeric_row.append(COLOR_MAP[cell])

        numeric_maze.append(numeric_row)

    plt.figure(figsize=(8, 8))
    plt.imshow(numeric_maze)
    plt.title(title)
    plt.axis('off')
    plt.show()
