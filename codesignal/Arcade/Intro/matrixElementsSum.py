#Sum all values in nested list
#tips: https://docs.python.org/3.8/tutorial/datastructures.html#nested-list-comprehensions
#And add some if condition to clean the value under 0
#Math:Permutation, Combination

def solution(matrix: list) -> int:
    """_summary_

    Args:
        matrix (list): input list
    """
    i = 0
    j = 0
    sum = 0
    # print(matrix)
    for i in matrix:
        # print(i)
        for j in i:
            if j != 0:
                sum = sum + j
            else:
                break
    return sum

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]
    print(solution(matrix))