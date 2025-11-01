def calc(n, cost):
    import networkx as nx

    g = nx.DiGraph()

    for i in range(n):
        for j in range(n):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if abs(di) + abs(dj) == 1:
                        if i + di in range(n) and j + dj in range(n):
                            g.add_edge((i, j), (i + di, j + dj), weight=cost(i + di, j + dj))

    return nx.shortest_path_length(g, source=(0, 0), target=(n - 1, n - 1), weight="weight")


from aocd import data

grid = data.split("\n")
grid = [[int(x) for x in row] for row in grid]
n = len(grid)

print(calc(n, lambda i, j: grid[i][j]))
print(calc(n * 5, lambda i, j: (grid[i % n][j % n] + (i // n) + (j // n) - 1) % 9 + 1))
