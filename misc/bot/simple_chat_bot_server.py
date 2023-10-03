import socket
import threading

# 設定伺服器IP和Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555

# 建立socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 綁定IP和Port
server_socket.bind((SERVER_IP, SERVER_PORT))

# 監聽連線
server_socket.listen(5)

print(f"[*] Listening on {SERVER_IP}:{SERVER_PORT}")

# 處理client的訊息
def handle_client(client_socket):
    while True:
        # 接收client訊息
        request = client_socket.recv(1024)

        # 將訊息轉換成大寫
        response = request.upper()

        # 回傳訊息
        client_socket.send(response)

# 循環接受client連線
while True:
    client_socket, addr = server_socket.accept()

    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    # 建立新執行緒處理client訊息
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()