import numpy as np

GUARD_STATES = [ord('^'), ord('>'), ord('V'), ord('<')]

def next_state(state):  
    return GUARD_STATES[(GUARD_STATES.index(state) + 1) % 4]

def gen_grid() -> np.ndarray:
    with open('./files/day6.txt') as f:
        lines = f.read().splitlines()
        return np.array([list(map(ord, line)) for line in lines])

def get_guard(grid: np.ndarray) -> tuple[int, int, int]:
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y][x] in GUARD_STATES:
                return x, y, grid[y][x]

def next_pos(x: int, y: int, state: int) -> tuple[int, int]:
    if state == ord('^'): return x, y - 1
    if state == ord('<'): return x - 1, y
    if state == ord('V'): return x, y + 1
    if state == ord('>'): return x + 1, y

def in_grid(x: int, y: int, grid: np.ndarray) -> bool:
    return 0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]

def try_move(x: int, y: int, state: int, grid: np.ndarray) -> tuple[int, int, int]:
    while True: 
        nx, ny = next_pos(x, y, state)
        if not in_grid(nx, ny, grid): return nx, ny, state
        if grid[ny, nx] != ord('#'):
            return nx, ny, state
        state = next_state(state)

def move_guard(grid: np.ndarray, x:int, y:int, state: int) -> tuple[np.ndarray, bool, int, int, int]:
    grid[y, x] = ord('X')
    nx, ny, state = try_move(x, y, state, grid)
    if in_grid(nx, ny, grid):
        grid[y, x] = ord('X')
        grid[ny, nx] = state
        return grid, False, nx, ny, state
    return grid, True, nx, ny, state

def part1() -> tuple[int, np.ndarray]:
    solved = solve_grid() 
    return np.sum(solved == ord('X'))

def solve_grid() -> np.ndarray:
    grid = gen_grid()
    x, y, state = get_guard(grid)
    while True:
        grid, done, x, y, state = move_guard(grid, x, y, state)
        if done: break
    return grid

def part2() -> int:
    def is_escapeable(gd, x:int, y:int, state:int) -> bool:
        seenpos = set()
        seenpos.add((x, y, state))
        while True:
            gd, done, x, y, state = move_guard(gd, x, y, state)
            if done: return True
            if (x, y, state) in seenpos: return False
            seenpos.add((x, y, state))
    
    grid = gen_grid()
    solved = solve_grid()
            
    starting_x, starting_y, starting_state = get_guard(grid)
    to_try_block = {(x,y) for x in range(solved.shape[1]) for y in range(solved.shape[0]) if solved[y][x] == ord('X')}
    to_try_block.remove((starting_x, starting_y))

    loops = 0 
    for blockx, blocky in to_try_block:
        gd = grid.copy()
        gd[blocky][blockx] = ord('#')
        if not is_escapeable(gd, starting_x, starting_y, starting_state): loops += 1
    return loops

def solve_day():
    print("===== DAY 06 =====")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__": 
    solve_day()
