# -*- coding:utf-8 -*-
"""
需求：给服务端发送给一个文本数据。
"""

import socket, sys
try:
    # 1.创建码头
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostbyname('localhost'), 10003))

    # 2.发送数据
    s.sendall("tcp ge men lai le")
    # 3.关闭
    s.close()
except socket.error:
    sys.exit()
