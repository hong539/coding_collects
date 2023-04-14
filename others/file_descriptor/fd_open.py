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