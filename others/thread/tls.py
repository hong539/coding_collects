import threading

#Play with ChatGPT
#請問Python程式語言有Thread-local storage的機制嗎?
#是的，Python提供了Thread-local storage的機制，稱為threading.local。Thread-local storage是一個線程內部的變數，每個線程都有自己獨立的副本，可以在線程內部訪問，但在不同線程之間是互不可見的。

mydata = threading.local()
mydata.x = 1  # 將變量x賦值給local對象的屬性

def func():
    mydata.x += 1
    print(mydata.x)

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()  # 執行線程t1
t2.start()  # 執行線程t2
t1.join()   # 等待線程t1執行完畢
t2.join()   # 等待線程t2執行完畢
