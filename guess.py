import random
import sys	# 系统模块

lucky = random.randint(0,101)
low, high = 0, 100
guess_limit, guess_count = int(sys.argv[1]), 0
# sys.argv[]  就是取从命令行传入的参数， 命令行输入 python guess.py  3----相当于传了guess.py 和 3这两个参数
# print(sys.argv)
# print(lucky)
guess = int(input(f'我想了一个幸运数字，范围是[{low},{high}],请你来猜一猜呀~\n温馨提示：只有{guess_limit}次尝试机会哦~请好好考虑后再开始猜数哈~\n'))
while (guess_limit > guess_count):
	guess_count += 1
	if lucky == guess:
		print("哇哦~你猜中了耶！恭喜你！")
		break
	elif lucky > guess and guess_count < guess_limit:
		low = guess
		guess = int(input(f"不好意思，幸运数字在({low},{high}]\n请继续--->"))
	elif lucky < guess and guess_count < guess_limit:
		high = guess
		guess = int(input(f"不好意思，幸运数字在[{low},{high})\n请继续--->"))
	else:
		print('不好意思，机会已经用完了，你没猜中。下次再来吧~88')


input('请输入任何字符，退出程序：')