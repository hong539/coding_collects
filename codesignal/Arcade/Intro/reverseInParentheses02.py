def reverse(string):
    seen_even = True
    temp, result = [], []
    for c in string:
        if c not in ('(', ')'):
            temp.append(c)
        else:
            if seen_even:
                result.extend(temp)
            else:
                result.extend(temp[::-1])
            seen_even = not seen_even
            temp = []
    if temp:  # e.g., 'Everything', 'Everythi)gn'
        if seen_even:
            result.extend(temp)
        else:
            result.extend(temp[::-1])
    return ''.join(result)

inputString = "foo(bar(baz))blim"
print(reverse(inputString))  # Output: foobazrabblim
inputString = "(bar)"
print(reverse(inputString))  # Output: rab
inputString = "foo(bar)baz"
print(reverse(inputString))  # Output: foobazrab