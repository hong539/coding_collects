def solution(inputString:str)->str:
    # creat temp string from inputString
    # reverse temp string
    # combine temp to result
    # return result
    print("inputString is:", inputString)
    temp = []
    for x in inputString:
        if x not in ("(", ")"):
            temp.append(x)
        else:
            continue
    print(temp)
    # temp = inputString.strip("(").strip(")")
    # reverse = temp[::-1]
    # print(reverse)
    # return reverse

if __name__ == "__main__":
    solution("(bar)")
    solution("foo(bar)baz")