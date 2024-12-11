def load_input() -> str:
    with open("./files/day9.txt") as f:
        return f.read().splitlines()[0]

def split_input(input: str) -> tuple[list[int], list[int]]:
    even, odd = [], []
    for i, x in enumerate(list(input)):
        if i % 2 == 0:
            even.append(int(x))
        else:
            odd.append(int(x))

    return even, odd

def gen_drive(first: list[int], second: list[int]) -> list[int]:
    if not first and not second:
        return []
    while len(first) != len(second):
        second.append(0)

    cnt = 0
    out = []
    for i in range(len(first) + len(second)):
        if i % 2 == 0:
            for _ in range(first[i//2]):
                out.append(cnt)
            cnt += 1
        else:
            for _ in range(second[(i-1)//2]):
                out.append(-1) 
    return out

def sort_drive(drive: list[int]) -> list[int]:
    sptr, eptr = 0, len(drive) - 1
    while sptr != eptr:
        if (drive[sptr] != -1):
            sptr += 1
        elif (drive[eptr] == -1):
            eptr -= 1
        else:
            drive[sptr], drive[eptr] = drive[eptr], drive[sptr]
            sptr += 1
            eptr -= 1   
    return drive

def sum_drive(drive: list[int]) -> int:
    return sum(val * i if val != -1 else 0 for i, val in enumerate(drive))

def find_continus_blocks(drive: list[int]) -> list[tuple[int, list[int]]]:
    """
    Finds all the data blocks inc -1 returning its symbol and cords of each block
    """
    blocks = []
    last = 'A'
    cds = []
    for i, val in enumerate(drive):
        if drive[i] != last:
            blocks.append((last, cds))
            last = drive[i]
            cds = [i]
        else:
            cds.append(i)
    blocks.append((last, cds))
    blocks.pop(0)
    return blocks
    

def de_frag(drive: list[int]) -> list[int]:
    def _defrag(drive: list[int], blocks: list[tuple[int, list[int]]], max:int ) -> list[int]:
        for j, (sym, crd) in reversed(list(enumerate(blocks))):
            if sym != -1 and crd[0] < max:
                for i, (symbol, negs) in enumerate(blocks):
                    if symbol == -1 and len(crd) <= len(negs) and i < j :
                        for k in range(len(crd)):
                            drive[negs[k]] = sym
                            drive[crd[k]] = -1
                        return drive, crd[0]
        return None, None
    max = len(drive)
    while True:
        blocks = find_continus_blocks(drive)
        tmp, max = _defrag(drive, blocks, max)
        if tmp == None:
            return drive
        drive = tmp
        
def part1() -> int:
    return sum_drive(sort_drive(gen_drive(*split_input(load_input()))))

def part2() -> int: 
    return sum_drive(de_frag(gen_drive(*split_input(load_input()))))

def solve_day() -> None:
    print("===== Day 09 =====")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    solve_day()
