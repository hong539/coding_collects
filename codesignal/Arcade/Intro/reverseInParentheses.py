def solution(inputString:str)->str:
    # creat temp string from inputString
    # reverse temp string
    # combine temp to result
    # return result
    print("inputString is:", inputString)
    temp = []
    final = []
    for x in inputString:
        if x not in ("(", ")"):
            temp.append(x)
        else:
            continue
    print(temp)
    print(temp[::-1])
    ss = final.extend(temp)
    print(ss)
    # return "".join(temp)
    # return "".join(temp[::-1])    
    # temp = inputString.strip("(").strip(")")
    # reverse = temp[::-1]
    # print(reverse)
    # return reverse

if __name__ == "__main__":
    solution("(bar)")
    solution("foo(bar)baz")
    # solution("foo(bar)baz(blim)")
    # solution("foo(bar(baz))blim")
    # solution("")
    # solution("()")
    # solution("(abc)d(efg)")