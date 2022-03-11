#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
from friendlist import *


def print_usage():
    print(f"欢迎使用Friend Book， 您可以输入以下命令： ")
    print(f"list: 显示名单")
    print(f"张三：查询张三的情况，李四同理。")
    print(f"886: 退出")


print_usage()
while True:
    cmd = input(f"请输入命令(“list”:显示用户列表 “名字 or 序号”：查看用户信息  “886”：退出程序)： ")
    if cmd == '886':
        print(f"再见啦~")
        break
    elif cmd == 'list':
        show_list()
    elif cmd == "record":
        show_record()
    else:
        find_name(cmd)