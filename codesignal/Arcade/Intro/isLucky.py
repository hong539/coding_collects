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