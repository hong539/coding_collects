#在 Linux 中，每個進程都有一些與之關聯的檔案描述符（file descriptor），用來表示進程正在使用的文件、網絡連接、管道等等。
# 文件描述符是一個非負整數，通過它可以實現對檔案、網絡套接字等資源的訪問和操作。
#檔案描述符在Linux中的應用非常廣泛，以下列出一些常見的用途：
#文件讀寫：使用 open 函數打開一個文件，可以得到一個文件描述符。之後使用 read 或 write 函數便可以通過文件描述符進行文件的讀寫。
# 打開文件
file = open("test.txt", "r")

# 獲取文件描述符
fd = file.fileno()

# 讀取文件
buf = bytearray(1024)
n = os.read(fd, len(buf))
while n > 0:
    print(buf[:n])
    n = os.read(fd, len(buf))

# 關閉文件
file.close()