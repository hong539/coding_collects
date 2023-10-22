def solution(a:list)->list:
    output = [0, 0]    
    if len(a) > 1:
        for x in range(0, len(a)):
            if x % 2:
                output[1] += a[x]
            else:
                output[0] += a[x]
        print(output)
        return output
    else:
        output[0] = a[0]        
        print(output)
        return output

if __name__ == "__main__":
    solution([50, 60, 60, 45, 70])
    solution([100, 50])
    solution([80])
    solution([100, 50, 50, 100])
    solution([100, 51, 50, 100])
    