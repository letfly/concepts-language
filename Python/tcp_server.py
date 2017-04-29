# -*- coding:utf-8 -*-
"""
需求：给服务端发送给一个文本数据。
"""

import socket, sys
try:
    # 1.创建码头。
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(('', 10003))
    ss.listen(1)
    # 2.连接码头。
    s, addr = ss.accept()
    print addr[0] + '.....connected'

    # 3.读取数据。
    data_in = s.recv(1024)
    print data_in
    # 4.关闭。
    s.close()
    ss.close()
except socket.error:
    sys.exit()
