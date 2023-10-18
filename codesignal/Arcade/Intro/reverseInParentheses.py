def solution(inputString:str)->str:
    # creat temp string from inputString
    # reverse temp string
    # combine temp to result
    # return result
    temp = inputString.strip('(').strip(')')
    reverse = temp[::-1]
    print(reverse)
    
    return reverse

if __name__ == "__main__":
    solution("(bar)")
    # solution("foo(bar)baz")
    # solution("foo(bar)baz(blim)")
    # solution("foo(bar(baz))blim")
    # solution("")
    # solution("()")
    # solution("(abc)d(efg)")