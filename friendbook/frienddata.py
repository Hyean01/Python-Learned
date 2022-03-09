#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import random
import pprint

names = []      # 人物名字
records = []    # 事件  张三 打了 李四 分数-1

xing = "罗、梁、 宋、唐、许、韩、冯、邓、曹、彭、曾、肖、田、董、袁、潘、于、蒋、蔡、余、杜、叶、 程、苏、魏、吕、丁、任、沈、 姚、卢、姜、崔、钟、谭、陆、汪、范、金、石、廖、 贾、夏、韦、付、方、白、邹、孟、熊、秦、邱、江、尹、薛、闫、段、雷、侯、龙、史、 陶、黎、贺、顾、毛、郝、龚、邵、万、钱、严、覃、武、戴、莫、孔、向、汤"
ming = "一、二、三、四、五、六、七、八、九、大、梦琪、忆柳、之桃、慕青、问兰、尔岚、元香、初夏、沛菡、傲珊、曼文、乐菱、痴珊、恨玉、惜文、香寒、新柔、语蓉、海安、夜蓉、涵柏、水桃、醉蓝、春儿、语琴"
add_score_things = "点赞、赞美、帮助、关爱、正确引导、送礼物、送花、刷火箭"       # 加分项
reduce_score_things = "打了、侮辱、辱骂、骂了、欺负、欺骗、错误引导、要挟、白嫖"    # 减分项


def mock_names():
    first_name_list = xing.replace(" ", "").split("、")
    last_name_list = ming.replace(" ", "").split("、")
    for i in range(1000):
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        name = first_name + last_name
        names.append(((i+1), name))
    return names


def mock_records():
    good_things = add_score_things.split("、")
    bad_things = reduce_score_things.split("、")
    things = good_things + bad_things
    for i in range(10000):
        # name1, name2 = random.choices(names, k=2)  # 随机抽取两个元素，有可能重复
        name1, name2 = random.sample(names, k=2)     # 随机抽取两个不重复的元素
        action = random.choice(things)
        if things.index(action) >= len(good_things):
            score = "分数 -1"
        else:
            score = "分数 +1"
        records.append((name1, action, name2, score))
    return records


def mock_data():
    print(f"start mocking data")
    mock_names()
    mock_records()
    print(f"finished mock data")


mock_data()

if __name__ == '__main__':
    mock_data()
    # pprint.pprint(names, indent=0)
    pprint.pprint(records)