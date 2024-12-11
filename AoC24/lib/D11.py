def load_stones() -> list[int]:
    with open("./files/day11.txt") as f:
        return list(map(int, f.read().splitlines()[0].split(" ")))

def list_to_key_cnt(l: list[any]) -> dict[any, int]:
    return {v: l.count(v) for v in set(l)}

def apply_rule(stone: int) -> tuple[int] | tuple[int, int]:
    if stone == 0:
        return (1,)
    elif len((ss := str(stone))) % 2 == 0:
        return (int(ss[:len(ss)//2]), int(ss[len(ss)//2:]))
    else:
        return (stone * 2024,)
    
def blinks(stones: list[int], n: int) -> dict[int,int]:
    stns = list_to_key_cnt(stones)
    for _ in range(n):
        ns = {}
        for stn, cnt in stns.items():
            for nv in apply_rule(stn):
                if nv in ns:
                    ns[nv] += cnt
                else:
                    ns[nv] = cnt
        stns = ns
    return stns

def slv(n: int) -> int:
    return sum(map(lambda kv: kv[1], blinks(load_stones(), n).items()))

def solve_day():
    print("=== Day 11 ===")
    print("Part 1:", slv(25))
    print("Part 2:", slv(75))

if __name__ == "__main__":
    solve_day()