# 創建管道
rfd, wfd = os.pipe()

# 創建子進程
pid = os.fork()

if pid == 0:
    # 子進程，關閉寫端，讀取數據
    os.close(wfd)
    data = os.read(rfd, 1024)
    print("Child process received:", data)
else:
    # 父進程，關閉讀端，寫入數據
    os.close(rfd)
    os.write(wfd, b"Hello, World!")