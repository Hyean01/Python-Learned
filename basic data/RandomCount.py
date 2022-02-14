# 实现自己的可循环类--随机数循环
# 循环的本质：iterable
# iter()这个函数进行循环，里面是调用 .__iter__()方法，返回一个iterator
# iterator() 需要有__next__()这个方法，就是下一个、下一个………………
# 所以要实现可循环，这个类里面必须要有__iter__()和__next__()这两个方法

import random


class RandomCount():
    def __iter__(self):
        return self

    def __next__(self):
        r = random.randint(1, 10)
        if (r==9):
            print("hahaha, you get '9'")
            raise StopIteration
        return r


if __name__ == "__main__":
    rc = RandomCount()
    for i in rc:
        print(i)