# import hashlib
#
#
# def get_md5_file(x):
#     """
#     生成哈希载药
#     :param x: r"路径"
#     :return: 哈希码
#     """
#     # md5 / sha1  / sha256
#     hasher = hashlib.md5()
#     with open(x, 'rb') as file:
#         file_iter = iter(lambda: file.read(1024), b'')
#         for i in file_iter:
#             hasher.update(i)
#     return hasher.hexdigest()
#

# !/usr/bin/env python

# -*- coding: cp936 -*-

import hashlib


def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src.encode("utf8"))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


if __name__ == '__main__':
    src = 'aaa'
    result_md5_value = get_md5_value(src)
    result_sha1_value = get_sha1_value(src)
    print('source string: ', src)
    print('MD5: ', result_md5_value)
    print('SHA1: ', result_sha1_value)
