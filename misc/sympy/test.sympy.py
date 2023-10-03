from sympy import *

# 設定符號變數
x, y, z = symbols('x y z')

# 解方程式
eq = Eq(x + y, 5)
result = solve(eq, (x, y))
print(result)  # Output: [(5 - y, y)]

# 算排列組合
n = 5
k = 3
result = binomial(n, k)
print(result)  # Output: 10

# 計算布林代數
a = symbols('a')
result = simplify((a & ~a) | (a & ~a & a))
print(result)  # Output: False