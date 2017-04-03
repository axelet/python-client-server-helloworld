import socket


if __name__ == "__main__":
    # req = b"Hello TCP!"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1235))
    while True:
        req = input().encode()
        if req == b"exit()":
            break
        s.send(req)
        response = s.recv(1024)
        print(response)
    s.close()
