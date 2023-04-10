#全域解釋器鎖（Global Interpreter Lock, GIL）
#Python在實作上採用GIL機制，限制同一時間只有一個執行序可以執行Python的bytecode。
# 當一個執行序被阻塞時，其他執行序就有機會執行。
# 這個機制可以保證Python的物件模型在多執行序的環境中能夠正常運作，但同時也導致Python的多執行序程式不能夠有效地利用多核心CPU的性能優勢。
import threading

def worker():
    for i in range(100000):
        pass

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
