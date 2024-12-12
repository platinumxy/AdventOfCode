import numpy as np
from functools import reduce

def load_garden() -> np.ndarray:
    with open("./files/testinput.txt") as f:
        return np.array([list(map(ord, l)) for l in f.read().splitlines()])
    
def cord_touching_group(garden: list[tuple[int,int]], cord: tuple) -> bool:
    for c in garden:
        if abs(c[0] - cord[0]) + abs(c[1] - cord[1]) == 1:
            return True
    return False

def cord_in_grid(garden: np.ndarray, cord: tuple[int,int]) -> bool:
    return 0 <= cord[0] < garden.shape[0] and 0 <= cord[1] < garden.shape[1]

def expand_group(garden: np.ndarray, group: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sym = garden[group[0][0], group[0][1]]
    return reduce(lambda acc, cord: acc + [(cord[0] + dy, cord[1] + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)] 
                                           if (cord[0] + dy, cord[1] + dx) not in acc and cord_in_grid(garden, (cord[0] + dy, cord[1] + dx)) 
                                           and garden[cord[0] + dy, cord[1] + dx] == sym], group, group)

def gen_groups(garden: np.ndarray) -> list[list[tuple[int, int]]]:
    def visit_cell(acc, cord):
        if cord in acc['visited']:
            return acc
        group = [(cord[0], cord[1])]
        last_len = 0
        while True:
            group = list(set(expand_group(garden, group)))
            if len(group) == last_len:
                break
            last_len = len(group)
        acc['groups'].append(group)
        acc['visited'].update(group)
        return acc

    return reduce(visit_cell, [(i, j) for i in range(garden.shape[0]) for j in range(garden.shape[1])], {'groups': [], 'visited': set()})['groups']


def get_group_area(group: list[tuple[int,int]]) -> int:
    return len(group)

def get_group_perimeter(group: list[tuple[int,int]]) -> int:
    return sum(1 for cord in group for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (cord[0] + dy, cord[1] + dx) not in group)

def calc_fence_cost(garden: np.ndarray) -> int:
    return sum(map(lambda x: get_group_area(x) * get_group_perimeter(x), gen_groups(garden)))

def num_sides(group: list[tuple[int,int]]) -> int:
    sds = [] 
    for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # find all sides pointing in that direction
        sides = [[cord] for cord in group if (cord[0] + dy, cord[1] + dx) not in group]
        last_len = 0
        while last_len != len(sides):
            if len(sides) == 1:
                break
            ns = [] 
            for i, s in enumerate(sides[:-1]):
                if any(cord_touching_group(s, cord) for cord in sides[i+1:]):
                    ns.extend(s)
                else:
                    ns.append(s)
            sides = ns
            last_len = len(sides)
        sds.extend(sides)
    return len(sds)
        
                

def part1():
    return calc_fence_cost(load_garden())

def part2():
    return (num_sides(gen_groups(load_garden())[0]))

def solve_day():
    print("====== Day 12 ======")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    solve_day()