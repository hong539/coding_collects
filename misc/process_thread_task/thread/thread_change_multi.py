#多進程
#在Python中，可以使用multiprocessing模組來創建多個進程，每個進程獨立運行，進程之間不共享內存，這樣就不受GIL的限制。
# 但進程之間的溝通需要使用IPC（Inter-process Communication）機制。
from multiprocessing import Process

def worker():
    for i in range(100000):
        pass

processes = []
for i in range(10):
    p = Process(target=worker)
    p.start()
    processes.append(p)

for p in processes:
    p.join()
