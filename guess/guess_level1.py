#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import sys  # 系统模块
import time


def input_limit_range():
    # 获取游戏开始的参数，猜测次数和范围
    # sys.argv[]  就是取从命令行传入的参数， 命令行输入 python guess.py  3----相当于传了guess.py 和 3这两个参数
    try:
        guess_limit, guess_range = int(sys.argv[1]), int(sys.argv[2])
    except:  # 异常处理模块
        guess_limit, guess_range = 3, 100
        print(f"输入值异常，使用默认值继续游戏！最多可猜测次数： {guess_limit}, 数字范围在 {guess_range}以内")
    return guess_limit, guess_range


def calc_time(begin_time):
    "计算每轮的耗时"
    end_time = time.time()
    use_time = round(end_time - begin_time, 2)
    print(f"本轮游戏耗时：{use_time}s")
    return use_time


def print_score(scores):
    best_score = min(scores, key=lambda x:x[2] if x[1] else 9999)
    print("===========战绩===========")
    for _cycle, _is_right, _use_time in scores:
        label = "胜利" if _is_right else "失败"
        best_label = "最棒" if (_cycle == best_score[0] and best_score[1]) else ""
        print(f"第{_cycle}轮, {label}, 用时 {_use_time}秒  {best_label}")
    print("==========================")