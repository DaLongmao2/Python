import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_socket.bind(('', 7799))
    # 目标信息
    ip = input('请输入服务器IP：')
    port = int(input('请输入服务器Port：'))
    # 链接套接字
    tcp_socket.connect((ip, port))

    file_name = input('请输入要下载的文件名:')
    # 发送文件请求
    tcp_socket.send(file_name.encode('utf-8'))
    # 接受发送的数据 最大接受1024
    recv_data = tcp_socket.recv(1024)
    # 如果接收到数据在创建文件，否则不创建
    if recv_data:
        with open("[接受]{}".format(file_name), 'wb') as f:
            f.write(recv_data)

    tcp_socket.close()


if __name__ == '__main__':
    main()