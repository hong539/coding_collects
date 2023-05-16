def solution(inputArray:list) -> list:
    #check string length in list
    #creat new list from longest strings
    #convert str to int
    #TypeError: can only concatenate str (not "int") to str
    #ValueError: invalid literal for int() with base 10: 'aba'
    result = []
    temp = len(max(inputArray, key=len))
    # print(temp)
    for l in inputArray:
        if len(l) == temp:
            result.append(l)
    # for i in range(0, len(inputArray)-1):
    #     item1 = inputArray[i]
    #     item2 = inputArray[i+1]
        
    #     if len(item1) == len(item2):
    #         result.append(item1)
    
    return result

if __name__ == "__main__":
    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    print(solution(inputArray))
    #output = ["aba", "vcd", "aba"]