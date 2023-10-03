# series
#Fisrt consider this series
# (1*1) + (2*2) + (3*3) + ... +(100 * 100) =?
#And if
# (7*7) + (9*9) + (11*11) + ... + (97 * 97) = ?

#method 1
#for loop
total = 0
for i in range(7, 98, 2):
    total += pow(i, 2)
print(total)

#method 2
#with Math Calculations by Sum of Squares of n Natural Numbers and sum of Arithmetic sequence
def sum(n):
    return (n+1)*(4*n**2+44*n+147)//3
print (sum(45))