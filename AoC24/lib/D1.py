def read_input() -> list[str]:
    with open('./files/day1.txt') as f:
        return f.read().splitlines()

def split_line(line: str) ->  tuple[int, int]:
    left, right = line.split("   ")
    return tuple(map(int, (left, right)))

def solve_day():
    lefts, rights = zip(*[split_line(line) for line in read_input()])
    lefts, rights = list(lefts), list(rights)

    lefts.sort()
    rights.sort()
    total_distance = sum(map(lambda t: abs(t[0] - t[1]), zip(lefts, rights)))

    similarity_score = sum(map(lambda l: rights.count(l) * l, lefts))
        
    print(f"=== Day One ===\nPart One: {total_distance}")  
    print(f"Part Two: {similarity_score}")

if __name__ == "__main__": 
    solve_day()
