def solution(inputString:str)->str:
    # creat temp string from inputString
    # reverse temp string
    # combine temp to result
    # return result
    print("inputString is:", inputString)
    seen_even = True
    temp = []
    result = []
    for x in inputString:
        # print("for loop here temp is:", temp)
        if x not in ('(', ')'):
            temp.append(x)            
        else:
            if seen_even:
                result.extend(temp)
            else:
                result.extend(temp[::-1])
            seen_even = not seen_even
            temp = []

    if temp:
        if seen_even:
            result.extend(temp)            
        else:
            result.extend(temp[::-1])            
    final = ''.join(result)
    print(final)
    return final

if __name__ == "__main__":
    # solution("(bar)")
    # solution("foo(bar)baz")
    # solution("foo(bar)baz(blim)")
    solution("foo(bar(baz))blim")
    # solution("")
    # solution("()")
    # solution("(abc)d(efg)")