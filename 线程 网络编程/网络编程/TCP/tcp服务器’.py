import socket


def main():
    # 创建套接字
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口号
    tcp_sever_socket.bind(('', 7788))

    # 监听客户端
    tcp_sever_socket.listen(128)

    while True:
        print('正在监听....')
        # 等待客户端链接
        new_client_socket, clientAdder = tcp_sever_socket.accept()
        print('成功监听....')
        while True:
            # 客户端 ip  rote
            print(clientAdder)
            # 接受客户端发送过来的数据
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode('utf-8'))
            if recv_data:
                # 回送消息给客户端
                new_client_socket.send('收到'.encode("utf-8"))
            else:
                break
        new_client_socket.close()

    # tcp_sever_socket.close()


if __name__ == '__main__':
    main()
