import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_surch(knot):
    if knot is None:
        return

    print(f"Ich bin bei Knoten: {knot.value}")

    dfs_surch(knot.left)

    dfs_surch(knot.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

dfs_surch(root)


def find_exit(maze, raw, colume, visit):
    number_of_raw, number_of_colume = len(maze), len(maze[0])

    if (
        raw < 0
        or colume < 0
        or raw >= number_of_raw
        or colume >= number_of_colume
        or maze[raw][colume] == 1
        or (raw, colume) in visit
    ):
        return False

    print(raw, colume)
    if raw == number_of_raw - 1 and colume == number_of_colume - 1:
        # definere das ziel !
        return True

    visit.add((raw, colume))

    top = find_exit(maze, raw - 1, colume, visit)
    down = find_exit(maze, raw + 1, colume, visit)
    left = find_exit(maze, raw, colume - 1, visit)
    right = find_exit(maze, raw, colume + 1, visit)

    return top or down or left or right


test_maze = [
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
]

print("way through maze is:", find_exit(test_maze, 0, 0, set()))


def flut_island(netz, raw, colume, visited):
    if (
        raw < 0
        or colume < 0
        or raw >= len(netz)
        or colume >= len(netz[0])
        or netz[raw][colume] == 0
        or (raw, colume) in visited
    ):
        return

    visited.add((raw, colume))

    flut_island(netz, raw + 1, colume, visited)
    flut_island(netz, raw - 1, colume, visited)
    flut_island(netz, raw, colume + 1, visited)
    flut_island(netz, raw, colume - 1, visited)


def zaehle_inseln(nets):
    visited = set()
    island_count = 0

    for row_index, row in enumerate(nets):
        for col_index, cell in enumerate(row):
            if cell == 1 and (row_index, col_index) not in visited:
                island_count += 1
                flut_island(nets, row_index, col_index, visited)
    return island_count


world_map = [[1, 1, 0, 0, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1]]
print("Anzahl der Inseln:", zaehle_inseln(world_map))


def generate_random_maze(rows, columes, wall_probability=0.3):
    maze = [[0 for _ in range(columes)] for _ in range(rows)]

    for raw in range(rows):
        for colume in range(columes):
            if random.random() < wall_probability:
                maze[raw][colume] = 1

    maze[0][0] = 0
    maze[rows - 1][columes - 1] = 0

    return maze


def print_maze(maze):
    for row in maze:
        # Ersetzt 1 durch '#' und 0 durch '.' für bessere Sichtbarkeit
        print(" ".join(["#" if cell == 1 else "." for cell in row]))


random_maze = generate_random_maze(5, 5, wall_probability=0.4)
print_maze(random_maze)

result = find_exit(random_maze, 0, 0, set())
print(f"Zufallslabyrinth lösbar? {result}")
