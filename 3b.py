import socket
import sys


def main():
    hostname, port = sys.argv[1], int(sys.argv[2])
    #hostname, port = 'telnet.iamroot.eu', 44553

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostname, port))
        cele = ''
        data = s.recv(1024)
        data = data.decode().rstrip()
        while data != '':
            cele += data
            data = s.recv(1024)
            data = data.decode().rstrip()
        KSI_index = cele.find('KSI')
        cele = cele[KSI_index:]
        print(repr(cele))
        cele = cele.replace('\x1B[1D*', '')
        cele = cele.split('\x1b[')
        print(cele)
        flag = cele[0]
        poss = len(flag)
        for i in range(1,len(cele)):
            if 'D' in cele[i]:
                i = cele[i].split('D')
                poss -= int(i[0])
                flag = flag[:poss] + i[1] + flag[poss+1:]
                poss += 1
            elif 'C' in cele[i]:
                i = cele[i].split('C')
                poss += int(i[0])
                flag = flag[:poss] + i[1] + flag[poss+1:]
                poss += 1
    
        print(flag)


if __name__ == '__main__':
    main()
    pass


#KSI{Why_do_you_let_me_lie_here_wastefully?}
def main2():
    print("\x1B[31mCervena", end='')
    print("\x1B[0m", end='')
    print(", ", end='')
    print("\x1B[34mmodra", end='\n')
    print("\x1B[0m", end='')
    
    print("pro \x1B7blazna dobra!", end='')
    print("\x1B8 soba \x1B[B", end='\n')
    
    print()
    input("Press Enter to continue...")

if __name__ == '__main__':
    main2()
    pass