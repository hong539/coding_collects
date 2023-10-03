#請問Python有哪些工具可以檢查程式碼的Time Complexity? 請提供範例程式碼
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 使用cProfile分析fibonacci函數的執行時間和呼叫次數
cProfile.run('fibonacci(10)')

# 這個程式碼使用cProfile分析fibonacci函數的執行時間和呼叫次數