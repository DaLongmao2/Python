import re


def main():
    names = ["ages", "_age", "1age", "a_age", "age_1", "_", "age!", "a#123"]
    for name in names:
        x = re.match(r"[a-zA-Z_][A-Za-z0-9_]*$", name)
        if x:
            print('符合规范{}'.format(name))
        else:
            print('不符合规范{}'.format(name))


if __name__ == '__main__':
    main()
