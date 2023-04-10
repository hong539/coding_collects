#Play with ChatGPT
#請問Python程式語言有Thread-local storage的機制嗎?
#是的，Python提供了Thread-local storage的機制，稱為threading.local。Thread-local storage是一個線程內部的變數，每個線程都有自己獨立的副本，可以在線程內部訪問，但在不同線程之間是互不可見的。

import threading

# 創建一個本地變數對象
local_data = threading.local()

# 定義一個函數
def func():
    # 設置本地變數的值
    local_data.value = 100
    # 獲取本地變數的值
    print(local_data.value)

# 創建兩個執行緒
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)

# 啟動執行緒
t1.start()
t2.start()

# 等待執行緒結束
t1.join()
t2.join()

