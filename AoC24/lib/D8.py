import numpy as np

FULLSTOP = np.char.array(['.'])[0]

def load_matrix() -> np.ndarray:
    with open("./files/day8.txt") as f:
        return np.array([list(line) for line in f.read().splitlines()])
    
def gen_fequency_table(mx: np.ndarray) -> dict[str, set[tuple[int, int]]]:
    tbl = {}
    for y in range(mx.shape[0]):
        for x in range(mx.shape[1]):
            if mx[y][x] not in tbl or np.char.equal(mx[y][x], FULLSTOP):
                tbl[mx[y][x]] = set()
            tbl[mx[y][x]].add((y, x))
    return tbl

def cord_in_mx(mx: np.ndarray, y: int, x:int) -> bool:
    return 0 <= y < mx.shape[0] and 0 <= x < mx.shape[1]

def part1() -> int:
    # I know this code wasnt the cleanest however I was CTFing all day and had to rush this
    mx = load_matrix()
    fq_table = gen_fequency_table(mx)

    anti_nodes = set()
    for cords in fq_table.values():
        if len(cords) == 1: continue
        for (y1, x1) in cords:
            for (y2, x2) in cords:
                if (y1, x1) == (y2, x2): continue
                new_y = y1 + 2 * (y2 - y1)
                new_x = x1 + 2 * (x2 - x1)
                if cord_in_mx(mx, new_y, new_x):
                    anti_nodes.add((new_y, new_x))
    return len(anti_nodes)

def part2() -> int:
    mx = load_matrix()
    fq_table = gen_fequency_table(mx)
    anti_nodes = set()
    for cords in fq_table.values():
        if len(cords) == 1:
            continue
        for (y1, x1) in cords:
            for (y2, x2) in cords:
                if (y1, x1) == (y2, x2):
                    continue
                new_y, new_x = y1 + (y2 - y1), x1 + (x2 - x1)
                while cord_in_mx(mx, new_y, new_x):
                    anti_nodes.add((new_y, new_x))
                    new_y += (y2 - y1)
                    new_x += (x2 - x1)
    return len(anti_nodes)

def solve_day():
    print("===== Day 08 =====")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    solve_day()
