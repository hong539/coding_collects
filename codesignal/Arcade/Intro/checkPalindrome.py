def solution(inputString):
    reverse = inputString[::-1]
    if reverse == inputString:
        return True
    return False  

if __name__ == "__main__":
    print(solution("abc"))
    print(solution("cbc"))
    print(solution("121"))
    print(solution("yay"))
    print(solution("123"))
    print(solution("我是我"))
    print(solution("他是他"))
    print(solution("我是他"))
    print(solution("她不是他"))