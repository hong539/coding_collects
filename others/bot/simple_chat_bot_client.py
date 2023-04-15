import socket

# 設定伺服器IP和Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555

# 建立socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連線到伺服器
client_socket.connect((SERVER_IP, SERVER_PORT))

# 傳送訊息
client_socket.send('hello server'.encode())

# 接收伺服器回傳的訊息
response = client_socket.recv(1024)

# 顯示伺服器回傳的訊息
print(response.decode())

# 關閉socket
client_socket.close()