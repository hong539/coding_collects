def solution(matrix):
    # return len(matrix)
    i = 0
    j = 0
    sum = 0
    for i in matrix:
        print(type(i))
        # print(i)
        for j in i:
            print(type(j))
            # print(j)

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]
    print(solution(matrix))