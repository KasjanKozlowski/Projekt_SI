from app.astar import astar
from app.heuristics import manhattan


def test_astar_finds_path():
    maze = [
        ['#', '#', '#', '#', '#'],
        ['#', 'S', '.', 'E', '#'],
        ['#', '#', '#', '#', '#'],
    ]

    start = (1, 1)
    end = (1, 3)

    path, visited = astar(maze, start, end, manhattan)

    assert path is not None
    assert len(path) > 0
    assert visited > 0


def test_astar_no_path():
    maze = [
        ['#', '#', '#', '#', '#'],
        ['#', 'S', '#', 'E', '#'],
        ['#', '#', '#', '#', '#'],
    ]

    start = (1, 1)
    end = (1, 3)

    path, visited = astar(maze, start, end, manhattan)

    assert path is None
