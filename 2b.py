import socket
import sys

def get_equation(res):
    result = ''
    for i in res:
        if i.isdigit() or i == '+':
            result += i
    return str(eval(result)).encode()

def main():
    data = ''
    hostname, port = sys.argv[1], int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostname, port))
        data = s.recv(1024)
        while 'KSI{' not in data.decode().rstrip() and 'Hmm' not in data.decode().rstrip():
            response = get_equation(data.decode().rstrip())
            s.sendall(response)
            data = s.recv(1024)
        else:
            print(data.decode().rstrip())

if __name__ == '__main__':
    try:
        sys.argv[1]
    except:
        exit()
    main()



#KSI{jak_je_tedy_sob_ve_dne_v_noci,_ktere_nepretrzite_musely_by_pocitat}