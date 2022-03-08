#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
from frienddata import *


def show_list():
    for n in names:
        print(f"{n[0]} {n[1]}")


def show_person(name):
    print(f"您要查找的用户信息是： {name}")
    show_record(name[0])


def find_name(name):
    # 根据输入的名字，查询是否在当前列表中，如果在，返回
    fname = [n for n in names if n[1] == name]
    if len(fname) == 0:
        print(f"系统不存在您要查找的用户，请检查输入或与用户确认是否已注册。")
    elif len(fname) == 1:
        show_person(fname[0])
    else:
        for n in fname:
            print(f"{n[0]}. {n[1]}")

        conf = True
        while conf:
            num = int(input(f"请输入名单中{fname}的一个序号，查看相关用户的具体记录： "))
            if num in dict(fname).keys():
                show_person((num, dict(fname)[num]))
            else:
                print("您的输入有误")
                conf = input(f"如果还想继续查看用户记录，请输入yes；输入其他将不再继续查看用户记录： ")
                if conf != 'yes':
                    conf = False


def show_record(id):
    personal_records = [r for r in records if r[0][0] == id]
    if personal_records:
        for r in personal_records:
            print(f"{r[0][1]} {r[1]} {r[2][1]}（No.{r[2][0]}）, {r[-1]}")
    else:
        print(f"暂无此用户的行为记录。")


def show_all_records():
    for r in records:
        print(f"{r[0][1]}(No.{r[0][0]}) {r[1]} {r[2][1]}（No.{r[2][0]}）, {r[-1]}")


if __name__ == '__main__':
    # show_all_records()
    print(random.sample.__doc__)