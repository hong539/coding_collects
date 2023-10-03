# 普通Python版本
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))

# 使用PyPy加速版本
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import sys
if '__pypy__' in sys.builtin_module_names:
    import __pypy__
    __pypy__.setrecursionlimit(100000)
    print(fibonacci(35))
else:
    print("Please run with PyPy")
