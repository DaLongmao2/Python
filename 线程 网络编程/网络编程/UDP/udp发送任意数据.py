import socket


def main():
    # 创建一个upd套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 从键盘获取数据
        x = input('请输入要发送的数据：\t')
        # 可以使用套接字收发数据
        # udp_socket.socket("haha", (ip, 端口))
        s.sendto(x.encode("utf-8"), ('192.168.232.1', 7788))
        if x == 'exit':
            break
    # 关闭套接字
    s.close()


if __name__ == '__main__':
    main()
