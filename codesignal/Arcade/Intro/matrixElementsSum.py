#Sum all values in nested list#tips: https://docs.python.org/3.8/tutorial/datastructures.html#nested-list-comprehensions
#And add some if condition to clean the value under 0
#tips: https://docs.python.org/3.8/tutorial/datastructures.html#nested-list-comprehensions
#tools: https://docs.python.org/3.8/library/pdb.html#module-pdb
# python3 -m pdb matrixElementsSum.py
# import pdb
#zip(): https://www.w3schools.com/python/ref_func_zip.asp

def solution(matrix: list) -> int:    
    """_summary_

    Args:
        matrix (list): input list
    """
    i = 0
    j = 0
    sum = 0
    unzip = zip(*matrix)
    # print(unzip)
    # print(list(unzip))
    for i in unzip:        
        # print(i)
        for j in i:
            # print(j)
            if j == 0:                
                break
            else:                
                # pdb.set_trace()                
                sum = sum + j    
    return sum

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]
    print(solution(matrix))