import time
from multiprocessing import Process
from threading import Thread

def cpu_task(number):
    result = sum(i * i for i in range(10**6))  # 模擬 CPU 密集型計算
    print(f"Task {number} completed.")

# 使用多執行緒
def multithreading_cpu():
    threads = []
    for i in range(4):  # 建立 4 個執行緒
        thread = Thread(target=cpu_task, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# 使用多處理
def multiprocessing_cpu():
    processes = []
    for i in range(4):  # 建立 4 個進程
        process = Process(target=cpu_task, args=(i,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

# 測試 CPU 密集型任務
if __name__ == "__main__":
    print("Testing multithreading for CPU-bound task...")
    start_time = time.time()
    multithreading_cpu()
    print(f"Multithreading Time: {time.time() - start_time:.2f} seconds")

    print("\nTesting multiprocessing for CPU-bound task...")
    start_time = time.time()
    multiprocessing_cpu()
    print(f"Multiprocessing Time: {time.time() - start_time:.2f} seconds")