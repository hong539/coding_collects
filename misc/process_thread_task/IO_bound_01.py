import time
from multiprocessing import Process
from threading import Thread

def io_task(number):
    time.sleep(2)  # 模擬 I/O 操作的延遲
    print(f"Task {number} completed.")

# 使用多執行緒
def multithreading_io():
    threads = []
    for i in range(4):  # 建立 4 個執行緒
        thread = Thread(target=io_task, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# 使用多處理
def multiprocessing_io():
    processes = []
    for i in range(4):  # 建立 4 個進程
        process = Process(target=io_task, args=(i,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

# 測試 I/O 密集型任務
if __name__ == "__main__":
    print("Testing multithreading for I/O-bound task...")
    start_time = time.time()
    multithreading_io()
    print(f"Multithreading Time: {time.time() - start_time:.2f} seconds")

    print("\nTesting multiprocessing for I/O-bound task...")
    start_time = time.time()
    multiprocessing_io()
    print(f"Multiprocessing Time: {time.time() - start_time:.2f} seconds")