#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com

# 函数三要素：名字、参数、返回值
#  返回值
# 1. 返回值可以有，也可以没有
# 2. 返回值用return返回，一个函数内可以有多个return，一旦遇到return，就结束
# 3. 可以返回多个值，直接逗号分隔即可，会包在一个元组里
# 传值 VS 传引用
# 1. 基本类型是传值        ---int/str/float等 函数不会改变原本变量的值
# 2. 其他类型是传引用       ----传过去的是变量的内存地址，例如list、tuple、dict、object
# 3. 复杂类型如何传值？

# 函数使用
# 1. 函数就是一个对象，有自己的属性，可以被赋值，可以被传递
# 2. 函数可以作为参数

# 匿名函数
# 1. 没有名称的一行函数 lambda

def bmi(height, weight):
    """
    计算BMI的值：身高/（体重*体重）
    身高是以米为单位，例如：1.78
    体重是以kg为单位，例如：60
    函数返回计算好的BMI值，保留2位小数
    """
    return round((weight/(height*height)), 2)


height = 1.57
def pre_height(height):
    # 传值
    return height+0.5


height_2= [1.57, 1.56, 1.72, 1.78]
def pre_height2(height):
    return (lambda x:x+0.5 for x in height)


def main(check):
    """以函数作为参数传递"""
    height = float(input("请输入你的身高（单位：米）： "))
    weight = float(input("请输入你的体重（单位：KG）： "))
    res = check(height, weight)
    print(f"结果是：{res}")
    return res


def process(numbers, calc):
    """lambda函数运用"""
    for n in numbers:
        print(calc(n), end=",")


if __name__ == '__main__':
    # print(bmi(1.53, 52))
    # print(bmi.__doc__)
    # print(height, pre_height(height))
    # print(height_2, pre_height2(height_2))
    # main(bmi)   # 以函数作为参数传递
    f = lambda x:x*x if x%3 == 0 else x+2
    process(range(13), f)