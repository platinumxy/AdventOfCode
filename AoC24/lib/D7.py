from itertools import product
from functools import reduce


def load_systems() -> list[tuple[int, list[int]]]:
    with open("./files/day7.txt") as f:
        return [(int(out), [int(x) for x in ins.split(" ")]) for out, ins in [sys.split(": ") for sys in f.read().splitlines()]]

def apply_op(a: int, op: str, b: int) -> int:
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "||":
        return int(str(a)+ str(b))
    else:
        raise ValueError(f"Unknown operator: {op}")

def can_sys_be_solved(target: int, values: list[int], op_types:list[str]) -> bool:    
    evaluate_expression = lambda ops, values: \
        reduce(lambda acc, val_op: apply_op(acc, val_op[1], val_op[0]), zip(values[1:], ops), values[0])
    return any(evaluate_expression(ops, values) == target for ops in list(product(op_types, repeat=len(values)-1)))

def part1() -> int:
    return sum(target for target, values in load_systems() if can_sys_be_solved(target, values, ["+", "*"]))

def part2() -> int:
    return sum(target for target, values in load_systems() if can_sys_be_solved(target, values, ["+", "*", "||"]))

def solve_day():
    print("===== Day 07 =====")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    solve_day()
