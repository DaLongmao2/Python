import socket


def main():
    # 创建一个upd套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 可以使用套接字收发数据
    # udp_socket.socket("haha", (ip, 端口))
    s.sendto(b"Yuan_Bin_Yin_Zao_Shang_Tiao_Le_100_Xia", ('192.168.232.1', 8000))
    # 关闭套接字
    s.close()


if __name__ == '__main__':
    main()
