def solution(picture:list)->list:
    # Get the length of the first string in the picture
    width = len(picture[0])
    
    # Add an asterisk to the beginning and end of each string in the picture
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    
    # Add a border of asterisks to the top and bottom of the picture
    border = "*" * (width + 2)
    picture.insert(0, border)
    picture.append(border)
    print(picture)
    return picture

if __name__ == "__main__":
    solution(["abc", 
              "ded"])
    solution(["a"])
    solution(["aa", 
              "**", 
              "zz"])
    solution(["abcde", 
              "fghij", 
              "klmno",
              "pqrst", 
              "uvwxy"])
    solution(["wzy**"])