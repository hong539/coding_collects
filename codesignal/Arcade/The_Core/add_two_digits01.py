# 10 ≤ n ≤ 99
def solution(n):
    sum = 0
    while (n != 0):
 
        sum = sum + int(n % 10)
        n = int(n/10)
 
    return sum

if __name__ == "__main__":
    print(solution(12))
    print(solution(29))
    print(solution(48))
    print(solution(10))
    print(solution(25))    
    # print(solution(01))
    print(solution(90))
    # WTF about n with negative sign?
    print(solution(-90))
    print(solution(-11))