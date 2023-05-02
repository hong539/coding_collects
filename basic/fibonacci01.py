def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # 使用生成器函數生成斐波那契數列
    fib = fibonacci()
    
    # 遍歷生成器，逐步生成數列值
    for i in range(10):
        print(next(fib))    