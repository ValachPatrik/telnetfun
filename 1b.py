import socket
import sys

def main():
    hostname, port = sys.argv[1], int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostname, port))
        data = s.recv(1024)
    print(data.decode().rstrip())


if __name__ == '__main__':
    main()