def solution(sequence):
    n = len(sequence)
    count = 0
    for i in range(1, n):
        if sequence[i] <= sequence[i-1]:
            count += 1
            if count > 1:
                return False
            if i > 1 and i < n-1 and sequence[i] <= sequence[i-2] and sequence[i+1] <= sequence[i-1]:
                return False
    return True

if __name__ == "__main__":
    print(solution([3, 6, -2, -5, 7, 3]))
    print(solution([-1, -2]))
    print(solution([5, 1, 2, 3, 1, 4]))
    print(solution([6, 9, -3]))