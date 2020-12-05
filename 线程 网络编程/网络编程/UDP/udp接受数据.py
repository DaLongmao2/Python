import socket


def main():
    while True:
        udp_docket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        local_adder = ('', 7788)
        udp_docket.bind(local_adder)
        demo, ip_port = udp_docket.recvfrom(1024)
        print("{} : {}".format(ip_port[0], demo.decode('utf-8')))
        if demo.decode('utf-8') == 'exit':
            print('已退出')
            break


if __name__ == '__main__':
    main()
