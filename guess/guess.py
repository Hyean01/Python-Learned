import random
import time
import guess_level1


# 获取本次游戏参数
guess_limit, guess_range = guess_level1.input_limit_range()
# 准备数据结构
cycle = 1  # 记录当前游戏轮数
score = []  # 记录每一轮的战绩
# 游戏执行
while True:
    lucky = random.randint(0, guess_range)
    print(f"即将开始第{cycle}轮数字游戏……祝你好运！本轮提示：幸运数字范围在[0, {guess_range}]\n"
          f"请开始--->", end= "")
    # 获取游戏开始时间
    begin_time = time.time()
    # 开始猜测
    for i in range(guess_limit):
        try:
            guess = int(input())
        except:
            print("你输入的值不符合，请输入数字哦")
            try:
                guess = int(input(f"请输入--->"))
            except:
                print(f"抱歉，输入有误，游戏将退出,谢谢参与。")
                break

        is_right = False
        if lucky == guess:
            is_right = True
            break
        elif lucky > guess:
            print("你猜的数字太小了", end=",")
        elif lucky < guess:
            print("你猜的数字太大了", end=",")
        if i < guess_limit - 1:
            print("请继续", end="--->")

    # 结果处理
    if is_right:
        print("*******哇哦~你猜中了耶！恭喜你！*******")
    else:
        print('不好意思，机会已经用完了，你没猜中。下次再来吧~88')

    # 计算本轮游戏耗时
    use_time = guess_level1.calc_time(begin_time)

    # 保存本轮战绩
    score.append((cycle, is_right, use_time))

    # 输出全部成绩
    guess_level1.print_score(score)

    # 战绩已记录，即将开始下一轮
    cycle += 1
    conf = input('如果想重新开始，请输入y，输入其他将退出游戏\n --->')
    if (conf != 'y'):
        print('欢迎下次再来~886')
        break
