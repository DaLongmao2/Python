import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input('请输入要链接的IP：')
    server_port = int(input('请输入要链接的Port：'))
    x = input('请输入要发送的数据：')
    tcp_socket.connect((server_ip, server_port))

    tcp_socket.send(x.encode('utf-8'))

    tcp_socket.close()


if __name__ == '__main__':
    main()