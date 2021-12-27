import random

lucky = random.randint(1,10)

guess = input('我想了一个幸运数字，你来猜一猜呀~\n')

if lucky == int(guess):
	print("哇哦~你猜中了耶！恭喜你！")
else:
	print("哎呀~这一次没猜中哦，继续加油！")
