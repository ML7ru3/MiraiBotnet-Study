import socket
import threading

def handle_client(client_socket):
    client_socket.send(b"Login: ")
    username = client_socket.recv(1024).strip()
    client_socket.send(b"Password: ")
    password = client_socket.recv(1024).strip()
    
    # Giả lập danh sách mật khẩu yếu của Mirai
    if b"admin" in username and b"admin" in password:
        client_socket.send(b"\nWelcome to IoT Device. BusyBox v1.1\n# ")
        # Giả lập việc Bot chờ lệnh từ C2
        while True:
            cmd = client_socket.recv(1024)
            if not cmd: break
    else:
        client_socket.send(b"Login incorrect\n")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 2323)) # Dùng port 2323 để tránh cần quyền root, hoặc 23 nếu sudo
server.listen(5)
print("[*] Mirai Honeypot listening on port 2323")

while True:
    client, addr = server.accept()
    print(f"[*] Connection from {addr}")
    threading.Thread(target=handle_client, args=(client,)).start()
