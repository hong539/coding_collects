def solution(matrix):    
    i = 0
    j = 0
    sum = 0
    #Sum all values in nested list
    #And add some if condition to clean the value under 0
    for i in matrix:
        for j in i:
            sum = sum + j
    return sum

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]
    print(solution(matrix))