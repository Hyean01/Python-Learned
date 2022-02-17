#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import random


def generate_answer():
    # 生成一个随机的4位数
    # return random.randint(1000, 9999)
    return 7845

def generate_guess():
    # guess number， enter by user
    guess = input("请输入一个4位数的数字：")
    return guess


def check_guess(answer, guess):
    # 校验guess的值是否正确，返回对应指示
    # check rule：数字和位置都一致，返回A；数字对但是数字位置不对，返回B，例如 9527， 9538，会返回2A0B
    answer = str(answer)
    guess = str(guess)
    if answer == guess:
        print("Congratulations! You Win!")
        return True
    else:
        count_A, count_B = 0, 0
        for index, char in enumerate(guess):
            if char == answer[index]:
                count_A += 1
            elif char != answer[index] and char in answer:
                count_B += 1
        print(f"本次猜测结果指示：{count_A}A{count_B}B")
        return False


def show_scores(scores):
    for x in scores:
        print(f"第{x[0]}轮结果  目标值：{x[1]}  猜测次数：{x[2]}    猜测结果：{'成功' if x[4] else '失败'}  游戏耗时：{x[3]}")


def should_continue():
    next_cycle = input('本轮游戏已结束。如果想重新开始，请输入y，输入其他将退出游戏\n --->')
    if (next_cycle != 'y'):
        print('欢迎下次再来~886')
        return False
    else:
        return True


# 自测
if __name__ == '__main__':
    res = check_guess(9572, 9772)
    print(res)