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
        
def gen_valid_updates() -> list[str]:
    global RULES, UPDATES
    return [update for update in UPDATES if valid_update(RULES, update)]

def gen_invalid_updates() -> list[str]:
    global RULES, UPDATES
    return [fix_invalid(RULES, update) for update in UPDATES if not valid_update(RULES, update)]

def fix_invalid(rules: dict[str, dict[str,list[str]]], l:list[str]) -> list[str]:
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

def solve_day():
    global RULES, UPDATES
    __rules, UPDATES = parse_input()
    RULES = gen_rules(__rules)
    print("=== Day 5: ===\nPart One:", calc_val(gen_valid_updates()), "\nPart Two:", calc_val(gen_invalid_updates())) 

if __name__ == "__main__": 
    solve_day()
