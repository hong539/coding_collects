#請問Python有哪些工具可以檢查程式碼的Time Complexity? 請提供範例程式碼
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

# 這個程式碼的時間複雜度為O(n)，其中n是arr列表的長度