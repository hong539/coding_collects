# Python program to
# compute sum of digits in
# number.

# Function to get sum of digits
def solution(n):	
	sum = 0
	for digit in str(n):
	    sum += int(digit)	
	return sum


if __name__ == "__main__":    
    # print(solution(-66))
    print(solution(66))
    print(solution(22))
    print(solution(10))
    print(solution(9))
    print(solution(1))
    # print(solution(-1))
    print(solution(12345))
