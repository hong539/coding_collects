def solution(year):
    return (year + 99) // 100

if __name__ == "__main__":
    print(solution(1905))
    print(solution(2023))
    print(solution(100000))