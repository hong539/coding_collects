def solution(inputArray:list) -> list:
    #check string length in list
    #creat new list from longest strings
    #convert str to int
    #ValueError: invalid literal for int() with base 10: 'aba'
    result = []
    for l in inputArray:
        # print(type(l))
        if len(int(l)) >= len(int(l+1)):
            result.append(l)
        else:
            break
    # print(result)
    return result

if __name__ == "__main__":
    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    print(solution(inputArray))