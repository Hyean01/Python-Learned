# for i in range(5):
#     print(i)


# 基于元组tuple/列表list的循环
def xunhuan():
    numbers = [2,4,13,34,11,23]
    numbers2 = ("lili", "lias", "haya", "yoy", "Hyo", "Hone")
    for name, age in zip(numbers2, numbers):
        print(name.ljust(4), ":", str(age).rjust(2))


def mutil_xunhuan():
    # 嵌套循环
    # 可以设置一个flag标记位来退出循环
    numbers = ["naudfs", "shdjsj", "shdkf"]
    is_found = False
    for name in numbers:
        if is_found:
            break
        for n in name:
            if n == 'j':
                # 碰到字符‘j’,就退出全部循环，通过break，退出当前循环；通过改变flag标记位，外层循环通过flag的值，判断是否退出循环
                is_found = True
                break
            print(name, n)


# homework
# homework-01
# 写一个for循环，从1到100，
# 如果是3的倍数输出“快”
# 如果是5的倍数输出“乐”
# 如果是3的倍数又是5的倍数，输出“Happy”
# 其他数字输出数字本身
def homework1():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("Happy", end=",")
        elif n % 3 == 0:
            print("快", end=",")
        elif n % 5 == 0:
            print("乐", end=",")
        else:
            print(n, end=",")


# homework-02
# 在homework-01的基础上，如果是7的倍数，什么都不做；如果是66，直接退出
def homework2():
    for n in range(1, 101):
        if n % 7 == 0:
            continue
        elif n == 66:
            break
        elif n % 3 == 0 and n % 5 == 0:
            print("Happy", end=",")
        elif n % 3 == 0:
            print("快", end=",")
        elif n % 5 == 0:
            print("乐", end=",")
        else:
            print(n, end=",")


def index_value():
    # 显示循环的index和值
    score = [98, 23, 89, 78, 80, 88, 90, 78, 100]
    for core in enumerate(score, start=1):
        print(core)


if __name__ == "__main__":
    # homework1()
    # print("+++++++++++++++++++++++")
    # homework2()
    # mutil_xunhuan()
    index_value()