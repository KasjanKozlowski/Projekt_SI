def load_maze(path):
    with open(path, "r", encoding="utf-8") as file:
        maze = [list(line.strip()) for line in file.readlines()]

    start = None
    end = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)

            if maze[i][j] == 'E':
                end = (i, j)

    return maze, start, end
