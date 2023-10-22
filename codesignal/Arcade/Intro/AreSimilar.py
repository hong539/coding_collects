def solution(a:list, b:list)->bool:
    if len(a) == len(b) and sum(a) == sum(b):
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == "__main__":
    solution([1, 2, 3],
             [1, 2, 3])
    solution([1, 2, 3],
             [2, 1, 3])
    solution([1, 2, 2],
             [2, 1, 1])
    solution([1, 2, 1, 2],
             [2, 2, 1, 1])
    solution([1, 2, 1, 2, 2, 1],
             [2, 2, 1, 1, 2, 1])
    solution([1, 1, 4],
             [1, 2, 3])
    solution([1, 2, 3],
             [1, 10, 2])
    solution([2, 3, 1],
             [1, 3, 2])
    solution([2, 3, 9],
             [10, 3, 2])
    solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
             [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])