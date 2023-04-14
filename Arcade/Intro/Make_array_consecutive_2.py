def solution(statues):
    statues.sort()
    count = 0
    for i in range(len(statues)-1):
        count += statues[i+1] - statues[i] - 1
    return count

if __name__ == "__main__":
    print(solution([6, 2, 3, 8]))
    print(solution([0, 3]))
    print(solution([1]))
    print(solution([0]))
    print(solution([-1]))
    print(solution([4.5]))
    print(solution([4, 5]))
    print(solution([4, 6]))