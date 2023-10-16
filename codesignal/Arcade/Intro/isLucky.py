def solution(n):
    sum = 0
    #convert int between str
    temp = str(n)
    for i in range(len(temp)):
        sum = sum + int(temp[i])
    print(sum)
    return True

if __name__ == "__main__":
    solution(1230)
    solution(239017)
    solution(134008)
    solution(10)
    solution(1010)
    solution(261534)
    solution(100000)
    solution(999999)
    solution(123321)