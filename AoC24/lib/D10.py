import numpy as np
from functools import reduce

def load_input() -> np.ndarray:
    with open("./files/day10.txt") as f:
        return np.array([list(map(int, line)) for line in f.read().splitlines()])

def find_trail_heads(mx: np.ndarray) -> list[tuple[int, int]]:
    return [(y, x) for y in range(mx.shape[0]) for x in range(mx.shape[1]) if mx[y, x] == 0]

def in_mx(mx: np.ndarray, y: int, x: int) -> bool:
    return 0 <= y < mx.shape[0] and 0 <= x < mx.shape[1]

def get_around(mx: np.ndarray, y: int, x: int) -> list[tuple[int, int]]:
    return [(y+dy, x+dx) for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] if in_mx(mx, y+dy, x+dx)]
    
def find_next(mx: np.ndarray, y: int, x: int) -> list[tuple[int, int]]:
    return [(ny, nx) for ny, nx in get_around(mx, y, x) if mx[ny, nx] == mx[y, x]+1]

def trails_from_head(mx: np.ndarray, pos: tuple[int, int]) -> int:
    assert mx[pos] == 0

    def visit(to_visit, visited):
        if not to_visit: return visited
        pos = to_visit.pop()
        visited.add(pos)
        return visit(to_visit + [next_pos for next_pos in find_next(mx, *pos)], visited)

    visited = visit([pos], set())
    return sum(1 for pos in visited if mx[pos] == 9)

def trail_steps(mx: np.ndarray, pos: tuple[int, int]) -> list[set[tuple[int, int]]]:
    assert mx[pos] == 0

    def visit(to_visit, visited):
        if not to_visit:
            return visited
        pos = to_visit.pop()
        visited[mx[pos]].add(pos)
        return visit(to_visit + find_next(mx, *pos), visited)

    visited = visit([pos], [set() for _ in range(10)])
    visited.pop(0)
    return visited

def trail_perms(mx: np.ndarray, pos: tuple[int, int], trails: list[set[tuple[int, int]]]) -> list[list[tuple[int, int]]]:    
    return reduce(lambda found, next_hight: \
                    [fnd + [cord] \
                    for fnd in found \
                    for cord in \
                    filter(lambda pos: pos in get_around(mx, *fnd[-1]), next_hight)], \
                    trails, [[pos]])

def part1(top_map: np.ndarray) -> int:
    return sum(map(lambda pos: trails_from_head(top_map, pos), find_trail_heads(top_map)))

def part2(top_map) -> int:
    return sum(len(trail_perms(top_map, heads, trail_steps(top_map, heads))) for heads in find_trail_heads(top_map))

def solve_day():
    top_map = load_input()
    print("=== Day 10 ===")
    print("Part 1:", part1(top_map))
    print("Part 2:", part2(top_map))

if __name__ == "__main__":
    solve_day()