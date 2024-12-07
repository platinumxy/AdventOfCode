import re as r

RX_MUL = r"mul\(([0-9]+?),([0-9]+?)\)"
RX_CONTROLED_MUL = r"(?P<mul>mul\(([0-9]+?),([0-9]+?)\))|(?P<do>do\(\))|(?P<dont>don't\(\))"

def read_file_str() -> str:
    with open('./files/day3.txt') as f:
        return f.read()

def get_all_muls() -> list[tuple[int, int]]:
    return [(int(l), int(r)) for (l, r) in (r.findall(RX_MUL, read_file_str())) if len(l) < 4 and len(r) < 4]

def get_all_controled_muls() -> list[tuple[int, int] | bool]:
    rx = r.finditer(RX_CONTROLED_MUL, read_file_str())
    results = []
    for m in rx:
        if m.group('mul'):
            results.append((int(m.group(2)), int(m.group(3))))
        elif m.group('do'):
            results.append(True)
        elif m.group('dont'):
            results.append(False)
    return results
        
def get_all_muls_sum() -> int:
    return sum([l * r for (l, r) in get_all_muls()])

def get_all_controled_muls_sum() -> int:
    muls = get_all_controled_muls()
    active = True
    sum = 0
    for i in range(len(muls)):
        match muls[i]:
            case (l, r):
                if active:
                    sum += l * r
            case True:
                active = True
            case False:
                active = False
    return sum

def solve_day():
    print(f"=== Day three ===\nPart One: {get_all_muls_sum()}\nPart Two: {get_all_controled_muls_sum()}")

if __name__ == "__main__": 
    solve_day()
