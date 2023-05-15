# src: https://www.w3schools.com/python/python_for_loops.asp

def main(matrix):
    for x in matrix:
        print(x)

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]
    main(matrix)