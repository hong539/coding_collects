# series
# (7*7) + (9*9) + (11*11) + ... + (97 * 97) = ?

sum = 0
for i in range(7, 98, 2):
    sum += i * i
print(sum)