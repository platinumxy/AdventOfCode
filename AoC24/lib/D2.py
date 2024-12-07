def get_reports() -> list[int]:
    with open('./files/day2.txt') as f:
        return map(lambda r: list(map(int, r.split(" "))), f.readlines())

def is_incrementing(arr: list[int]) -> bool:
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

def is_decrementing(arr: list[int]) -> bool:
    return all(arr[i] > arr[i+1] for i in range(len(arr)-1))

def diff_check(arr: list[int]) -> bool:
    return all(abs(arr[i] - arr[i+1]) < 4 for i in range(len(arr)-1))    

def valid_report(arr: list[int]) -> bool:
    return (is_incrementing(arr) or is_decrementing(arr)) and diff_check(arr)

def dampened_check(arr: list[int]) -> bool:
    return valid_report(arr) or any(valid_report(arr[:i] + arr[i+1:]) for i in range(len(arr)))

def solve_day():
    valid_count = len(list(filter(valid_report, get_reports())))
    valid_dampened_count = len(list(filter(dampened_check, get_reports())))

    print(f"=== Day two ===\nPart One: {valid_count}\nPart Two: {valid_dampened_count}")

if __name__ == "__main__":
    solve_day()
