def load_matrix() -> list[list[str]]:
    with open('./files/day4.txt') as f:
        return [list(l.strip()) for l in f.readlines()]

def extract_points(matrix: list[list[str]], points: list[tuple[int, int]]) -> str | None:
    extracted_points = [matrix[x][y] for x, y in points if 0 <= x < len(matrix) and 0 <= y < len(matrix[0])]
    return "".join(extracted_points) if len(extracted_points) == len(points) else None

def gen_permutations(matrix: list[list[str]], i:int, j:int) -> list[str | None]:
    return [extract_points(matrix, rotation) for rotation in [
        [(i, j), (i, j+1), (i, j+2), (i, j+3)],
        [(i, j), (i, j-1), (i, j-2), (i, j-3)],
        [(i, j), (i+1, j), (i+2, j), (i+3, j)],
        [(i, j), (i-1, j), (i-2, j), (i-3, j)],
        [(i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)],
        [(i, j), (i-1, j-1), (i-2, j-2), (i-3, j-3)],
        [(i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3)],
        [(i, j), (i-1, j+1), (i-2, j+2), (i-3, j+3)],
    ]]

def xmases(matrix: list[list[str]], i:int, j:int) -> int:
    return sum(p == "XMAS" for p in gen_permutations(matrix, i, j))

def count_xmas(matrix: list[list[str]]) -> int:
    return sum(xmases(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
                

def generate_x_mas(matrix: list[list[str]], i: int, j: int) -> list[str]:
    return [extract_points(matrix, rotation) for rotation in [
        [(i, j), (i, j+2), (i+1, j+1), (i+2, j), (i+2, j+2)], # evil matrixes
        [(i, j), (i, j-2), (i+1, j-1), (i+2, j), (i+2, j-2)], # this checks to many same 
        [(i, j), (i+2, j), (i+1, j+1), (i, j+2), (i+2, j+2)], # cases meaning therell be
        [(i, j), (i+2, j), (i+1, j-1), (i, j-2), (i+2, j-2)], # double expected 
        [(i, j), (i, j+2), (i-1, j+1), (i-2, j), (i-2, j+2)], # however i dont want to
        [(i, j), (i, j-2), (i-1, j-1), (i-2, j), (i-2, j-2)], # re write by hand the indexes
        [(i, j), (i-2, j), (i-1, j+1), (i, j+2), (i-2, j+2)], # so we have quick and dirty 
        [(i, j), (i-2, j), (i-1, j-1), (i, j-2), (i-2, j-2)], # fix of /2 in cont_x_mas
        ]]

def x_masses(matrix: list[list[str]], i:int, j:int) -> int:
    return sum(p == "MSAMS" for p in generate_x_mas(matrix, i, j))

def count_x_mas(matrix: list[list[str]]) -> int:
    return sum(x_masses(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))) // 2

def solve_day():
    print("=== Day 4: ===\nPart One:", count_xmas(load_matrix()),"\nPart Two:", count_x_mas(load_matrix()))

if __name__ == "__main__": 
    solve_day()
