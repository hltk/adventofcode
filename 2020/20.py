import collections
import dataclasses
import itertools
import math


@dataclasses.dataclass
class Tile:
    grid: list[str]
    index: str
    placed: bool = False

    @property
    def sides(self):
        return [
            self.grid[0],
            ''.join(list(zip(*self.grid))[-1]),
            self.grid[-1],
            ''.join(list(zip(*self.grid))[0])
        ]

    def rot(self):
        self.grid = list(reversed(list(map(''.join, zip(*self.grid)))))

    def flip(self):
        self.grid = list(reversed(self.grid))

    def all_rots(self):
        for _ in range(2):
            for _ in range(4):
                yield
                self.rot()
            self.flip()


def main(inp):
    tiles = []
    for t in inp.split('\n\n'):
        i = t[5:t.index(':')]
        t = t.split('\n')[1:]
        tiles.append(Tile(t, i))

    def unique(side):
        return min(side, side[::-1])

    edges = collections.defaultdict(int)
    for t in tiles:
        for side in t.sides:
            side = unique(side)
            edges[side] += 1

    corners = [t.index for t in tiles
               if sum(edges[side] == 1 for side in map(unique, t.sides)) == 2]
    print(eval('*'.join(corners)))


    side = round(math.sqrt(len(tiles)))
    grid = [[None] * side for _ in range(side)]

    for i, j in itertools.product(range(side), repeat=2):
        for tile in filter(lambda x: x.placed is False, tiles):
            def good():
                top, side = tile.sides[0], tile.sides[3]
                if i == 0 and j == 0:
                    top = unique(top)
                    side = unique(side)
                    return edges[top] == 1 and edges[side] == 1
                if i == 0:
                    return side == grid[i][j - 1].sides[1]
                return top == grid[i - 1][j].sides[2]

            for _ in tile.all_rots():
                if good():
                    grid[i][j] = tile
                    tile.placed = True
                    break
            if tile.placed:
                break

    def peel(g):
        return [''.join(x for x in row[1:-1]) for row in g[1:-1]]

    grid = [[peel(x.grid) for x in row] for row in grid]
    grid = [[''.join(x) for x in zip(*row)] for row in grid]
    grid = [x for row in grid for x in row]

    n = len(grid)
    grid = Tile(grid, None)

    seamonster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]

    sn, sm = len(seamonster), len(seamonster[0])
    points = [(i, j) for i, j in itertools.product(range(sn), range(sm))
              if seamonster[i][j] == '#']

    for _ in grid.all_rots():
        r = 0
        for i, j in itertools.product(range(n - sn + 1), range(n - sm + 1)):
            if {grid.grid[i + si][j + sj] for si, sj in points} == {'#'}:
                r += ''.join(seamonster).count('#')
        if r:
            print(''.join(grid.grid).count('#') - r)


from aocd import data
main(data)
