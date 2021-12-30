import random
import sys	# 系统模块
import time

guess_limit, guess_range = int(sys.argv[1]), int(sys.argv[2])
# sys.argv[]  就是取从命令行传入的参数， 命令行输入 python guess.py  3----相当于传了guess.py 和 3这两个参数
# print(sys.argv)
# print(lucky)
cycle = 1 # 记录当前游戏轮数
score = [] # 记录每一轮的战绩
while True:
	# generate a lucky number
	lucky = random.randint(0,guess_range)
	low, high = 0, guess_range
	print(f"即将开始第{cycle}轮数字游戏……祝你好运！")
	begin_time = time.time()
	guess = int(input(f'我想了一个幸运数字，范围是[{low},{high}],请你来猜一猜呀~\n温馨提示：只有{guess_limit}次尝试机会哦~请好好考虑后再开始猜数哈~\n'))
	for i in range(1, guess_limit):
		is_right = False
		# guess_count += 1
		if lucky == guess:
			is_right = True
			break
		elif lucky > guess:
			low = guess
			guess = int(input(f"不好意思，幸运数字在({low},{high}]\n请继续--->"))
		elif lucky < guess and guess < 101:
			high = guess
			guess = int(input(f"不好意思，幸运数字在[{low},{high})\n请继续--->"))
		else:
			guess = int(input(f"不好意思，幸运数字在[{low},{high})\n请继续--->"))

			

	# 结果处理
	if is_right:
		print("*******哇哦~你猜中了耶！恭喜你！*******")
	else:
		print('不好意思，机会已经用完了，你没猜中。下次再来吧~88')

	end_time = time.time()
	use_time = round((end_time - begin_time),3)
	print(f'本轮游戏共耗时：{use_time}秒')

	# 保存战绩
	score.append((cycle, is_right, use_time))
	print("===========战绩===========")
	for _cycle, _is_right, _use_time in score:
		label = "胜利✌" if _is_right else "失败😢"
		print(f"第{_cycle}轮, {label}, 用时 {_use_time}秒")
	print("==========================")

	cycle += 1 # 战绩已记录，即将开始下一轮
	conf = input('如果想重新开始，请输入y，输入其他将退出游戏\n --->')
	if (conf != 'y'):
		print('欢迎下次再来~886')
		break