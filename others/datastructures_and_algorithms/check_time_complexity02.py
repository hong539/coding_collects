#請問Python有哪些工具可以檢查程式碼的Time Complexity? 請提供範例程式碼
import timeit

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# 測量factorial函數執行時間
execution_time = timeit.timeit(lambda: factorial(5), number=1000)
print("Execution Time:", execution_time)

# 這個程式碼測量factorial函數的執行時間，並將結果打印出來