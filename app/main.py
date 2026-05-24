from maze import load_maze
from astar import astar
from heuristics import manhattan, euclidean, zero
from visualization import print_maze, visualize
import time


HEURISTICS = {
    "Manhattan": manhattan,
    "Euclidean": euclidean,
    "Zero": zero,
}


def run_test(maze_path: str):
    maze, start, end = load_maze(maze_path)

    print("=" * 60)
    print(f"Labirynt: {maze_path}")
    print("=" * 60)

    for name, heuristic in HEURISTICS.items():
        start_time = time.perf_counter()

        path, visited = astar(maze, start, end, heuristic)

        end_time = time.perf_counter()

        duration = end_time - start_time

        print(f"\nHeurystyka: {name}")
        print(f"Czas: {duration:.6f} s")
        print(f"Odwiedzone pola: {visited}")

        if path:
            print(f"Długość ścieżki: {len(path)}")
            print_maze(maze, path)
            visualize(maze, path, title=f"{name} - {maze_path}")
        else:
            print("Nie znaleziono ścieżki")


if __name__ == "__main__":
    mazes = [
        "data/maze1.txt",
        "data/maze2.txt",
        "data/maze3.txt",
    ]

    for maze in mazes:
        run_test(maze)
