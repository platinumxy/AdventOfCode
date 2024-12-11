def read_input() -> list[str]:
    with open('./files/day1.txt') as f:
        return f.read().splitlines()

def split_line(line: str) ->  tuple[int, int]:
    left, right = line.split("   ")
    return tuple(map(int, (left, right)))

def part1() -> int:
    lefts, rights = zip(*[split_line(line) for line in read_input()])
    lefts, rights = list(lefts), list(rights)

    lefts.sort()
    rights.sort()
    return sum(map(lambda t: abs(t[0] - t[1]), zip(lefts, rights)))

def part2() -> int: 
    lefts, rights = zip(*[split_line(line) for line in read_input()])
    lefts, rights = list(lefts), list(rights)
    lefts.sort()
    rights.sort()
    return sum(map(lambda l: rights.count(l) * l, lefts))

def solve_day():        
    print("===== Day 01 =====")
    print(f"Part One: {part1()}")  
    print(f"Part Two: {part2()}")

if __name__ == "__main__": 
    solve_day()
