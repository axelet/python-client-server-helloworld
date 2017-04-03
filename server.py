import socket
from select import select

def bind_socket(port):
    s = socket.socket()
    s.bind(("127.0.0.1", int(port)))
    s.listen(10)
    conn, addr = s.accept()
    return conn
    # while True:
    #     conn, addr = s.accept()
    #     while True:
    #         data = conn.recv(1024)
    #         if not data or data == "close":
    #             break
    #         print("Port {}: {}".format(port, data))
    #         conn.send(data)
    #     conn.close()

if __name__ == "__main__":
    readsocks = [bind_socket(x) for x in ["1234", "1235"]]
    writesocks = readsocks

    while True:
        readables, writeables, exceptions = \
            select(readsocks, [], [])
        for sockobj in readables:
            data = sockobj.recv(512)
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                print(id(sockobj), ":", data)
