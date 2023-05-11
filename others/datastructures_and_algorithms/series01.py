# series
#Fisrt consider this series
# (1*1) + (2*2) + (3*3) + ... +(100 * 100) =?
#And if
# (7*7) + (9*9) + (11*11) + ... + (97 * 97) = ?

def square(num) :
    sum = 0
    for i in range(1, num+1) :
        sum= sum + (i * i)
    return sum
num = 6
print("Sum of square is:",square(num))