#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import random
import pprint

xing = "罗、梁、 宋、唐、许、韩、冯、邓、曹、彭、曾、肖、田、董、袁、潘、于、蒋、蔡、余、杜、叶、 程、苏、魏、吕、丁、任、沈、 姚、卢、姜、崔、钟、谭、陆、汪、范、金、石、廖、 贾、夏、韦、付、方、白、邹、孟、熊、秦、邱、江、尹、薛、闫、段、雷、侯、龙、史、 陶、黎、贺、顾、毛、郝、龚、邵、万、钱、严、覃、武、戴、莫、孔、向、汤"
ming = "一、二、三、四、五、六、七、八、九、大、梦琪、忆柳、之桃、慕青、问兰、尔岚、元香、初夏、沛菡、傲珊、曼文、乐菱、痴珊、恨玉、惜文、香寒、新柔、语蓉、海安、夜蓉、涵柏、水桃、醉蓝、春儿、语琴"
add_score_things = "点赞、赞美、帮助、关爱、正确引导、送礼物、送花、刷火箭"       # 加分项
reduce_score_things = "打了、侮辱、辱骂、骂了、欺负、欺骗、错误引导、要挟、白嫖"    # 减分项
names = []      # 人物名字
records = []    # 事件  张三 打了 李四 分数-1
name_dict = {}  # 人物和事件记录，
score_dict = {} # 人物分数汇总


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
            score = "-1"
        else:
            score = "+1"
        records.append((name1, action, name2, score))
    return records


def build_name():
    """构建人物事件字典，一个人物会有多个记录，例如： {998：[recored1, recored2, ……]}"""
    for r in records:
        my_id = r[2][0]
        if my_id in name_dict.keys():
            name_dict[my_id].append(r)
        else:
            name_dict[my_id] = [r]


def build_score():
    """每个人根据其相关事件，统计分数，基础分100， 例如{(998,李四）：{(112, 李毅):87, (113, 李玉):99, ……}}"""
    for r in records:
        account = r[2][0]   # 账户统计者
        actioner = r[0][0]  # 对账户统计者施加行为的人
        score = eval(r[3])  # 该事件造成的分数变动, 用eval()是因为 之前的分数用的是字符串，这样就可以去掉引号，成为数值
        if account in score_dict.keys():
            account_recore_id = score_dict[account].keys()  # score_dict[account]得出来的还是一个dict
            if actioner in account_recore_id:
                score_dict[account][actioner] += score
            else:
                score_dict[account][actioner] = 100 + score
        else:
            score_dict[account] = {actioner:100 + score}


def mock_data():
    print(f"start mocking data")
    mock_names()
    mock_records()
    build_name()
    build_score()
    print(f"finished mock data")


mock_data()

if __name__ == '__main__':
    mock_data()
    # pprint.pprint(names, indent=0)
    pprint.pprint(records)