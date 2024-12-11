def parse_input() -> tuple[list[tuple[str, str]], list[list[str]]]:
    with open('./files/day5.txt') as f:
        lines = f.read().splitlines()
        split = lines.index("")
        lhs = [tuple(line.split("|")) for line in lines[:split]]
        rhs = [line.split(",") for line in lines[split+1:]]
        return lhs, rhs

def gen_rules(rs: list[tuple[str, str]]) -> dict[str, dict[str, list[str]]]:
    d = {k: {"smaller": [], "larger": []} for pair in rs for k in pair}
    for sm, lg in rs:
        d[sm]["larger"].append(lg)
        d[lg]["smaller"].append(sm)
    return d

def valid_update(rules: dict[str, dict[str, list[str]]], update: list[str]) -> bool:
    return all(
        not ((check in rules[val]["smaller"] and j > i) or (check in rules[val]["larger"] and j < i))
        for i, val in enumerate(update)
        for j, check in enumerate(update)
    )
        
def gen_valid_updates(rules: dict[str, dict[str, list[str]]], updates: list[list[str]]) -> list[list[str]]:
    return [update for update in updates if valid_update(rules, update)]

def gen_invalid_updates(rules: dict[str, dict[str, list[str]]], updates: list[list[str]]) -> list[list[str]]:
    return [fix_invalid(rules, update) for update in updates if not valid_update(rules, update)]

def fix_invalid(rules: dict[str, dict[str, list[str]]], l: list[str]) -> list[str]:
    out = []
    for val in l:
        for i, check in enumerate(out):
            if check in rules[val]["larger"]:
                out.insert(i, val)
                break
        else:
            out.append(val)
    return out

def calc_val(l: list[any]) -> int:
    return sum(map(lambda l: int(l[len(l)//2]), l))

def part1() -> int:
    rules, updates = parse_input()
    rules_dict = gen_rules(rules)
    return calc_val(gen_valid_updates(rules_dict, updates))

def part2() -> int:
    rules, updates = parse_input()
    rules_dict = gen_rules(rules)
    return calc_val(gen_invalid_updates(rules_dict, updates))

def solve_day():
    print("===== Day 05: =====")
    print(f"Part One: {part1()}")
    print(f"Part Two: {part2()}") 

if __name__ == "__main__": 
    solve_day()
