#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import time
from guess_util import *


next_cycle = True

cycle = 0
while next_cycle:
    # 生成目标值
    answer = generate_answer()
    # 准备数据结构
    guess_limit = 3
    guess_count = 1
    cycle += 1
    begin_time = time.time()
    scores = []

    # 用户输入猜测值
    while guess_limit:
        guess = generate_guess()
        # check answer和guess是否匹配
        result = check_guess(answer=answer, guess=guess)

        # 结果处理
        if result or guess_limit == 1:
            end_time = time.time()
            use_time = round((end_time - begin_time), 2)
            break
        else:
            guess_limit -= 1
            guess_count += 1
    scores.append((cycle, answer, guess_count, use_time, result))

    # 输出结果
    show_scores(scores)


    # 是否继续下一轮猜数字游戏
    next_cycle = should_continue()


