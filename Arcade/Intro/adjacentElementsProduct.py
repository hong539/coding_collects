
def solution(inputArray):
    length = len(inputArray)      
    sum = []     
    for i in range(length-1):        
        sum.append(inputArray[i] * inputArray[i+1])
    return max(sum)

if __name__ == "__main__":
    print(solution([3, 6, -2, -5, 7, 3]))
    print(solution([-1, -2]))
    print(solution([5, 1, 2, 3, 1, 4]))
    print(solution([6, 9, -3]))