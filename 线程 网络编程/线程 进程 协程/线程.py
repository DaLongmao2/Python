import time
import threading


def sing():
    for i in range(5):
        print('正在喝茶')
        time.sleep(1)


def jmp():
    for i in range(5):
        print('正在跳舞')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=jmp)
    # 启动线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()