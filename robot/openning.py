import datetime
import requests
import json

def hello(name = 'HAHA', lang = 'Python'):
	# print('我是HAHA,我爱用python')
	print('你好，我是{},我爱用{}\n'.format(name, lang))
	input("你叫什么名字呢？\n --->")

def run_nian(year):
	return (year%4==0 and year%100!=0) or (year%400==0)

def show_robot():
	print('''	      \_/
	     (* *)
	    __)#(__
	   ( )...( )(_)
	   || |_| ||//
	>==() | | ()/
	    _(___)_
	   [-]HAHA[-]\n''')


def ask():
	age = input("我今年8岁了,你呢？\n ---->")
	if int(age) <18:
		print(f"呀！你也只是个{age}岁的孩子呀，我们一样耶~~")
	elif int(age) >= 18 and int(age) < 30:
		print(f'哇！你已经{age}岁了，肯定是个青春阳光的青少年！')
	elif int(age) >= 30:
		print(f'哇！你已经{age}岁了，肯定经历丰富，有很多故事吧~')
	else:
		print(f"呜呜呜~你年龄是不是输错了呢？人家只认识数字哦~你输入的是{age}")

def show_time():
	# dt =datetime.datetime.now()# 获取当前时间
	print(datetime.datetime.now().strftime('HAHA： 你是想知道当前时间么？\nHAHA：今天是:%Y年%m月%d日 %H:%M:%S'))

def seprate():
	print('-------------------------------')

def exit():
	print('你确定要退出当前对话么？yes/no')


def contact():
	print('我是HAHA， 您有什么吩咐么？')
	while True:
		print('-------------------------------')
		order = input('我：')
		if order in ['time', '日期', '时间']:
			show_time()

		elif order in ['weather', '天气', '气象','温度','天气预报']:
			city = input("HAHA:你想查看哪个城市的天气预报呢？\n我：")
			weather(city)

		elif order in ['88', 'Bye', '拜拜', '拜','exit']:
			confirm = input('HAHA：你确定要退出当前对话么？yes/no\n我：')
			if confirm == 'yes':
				print('HAHA：好的，有需要再找我哦，88！')
				break

		else:
			print(ai_talk(order))
			# print('呜呜呜~~我还没学习到，对不起，不能完成你的吩咐，我会继续努力的~')


def ai_talk(question):
	return 'HAHA:' + question.replace('你','我').replace('不', '').replace('吗', '').replace('？', '！').replace('不', '')


def weather(city='深圳'):
	data = {'appid':'73495343', 'appsecret':'9xPUv2S6','version':'v9','city':{city}}
	res = requests.get(url='https://www.yiketianqi.com/api/', params=data)
	res_text = res.text
	res_json = json.loads(res_text)
	weather = res_json['data'][0]['wea']
	temperature = res_json['data'][0]['tem']
	humidity = res_json['data'][0]['humidity']
	pressure = res_json['data'][0]['pressure']
	air_level = res_json['data'][0]['air_level']
	air_tips = res_json['data'][0]['air_tips']
	alert = res_json['data'][0]['alarm']['alarm_content']
	print(f"{city}的温度是：{temperature}℃, 天气是：{weather}, 湿度：{humidity}, 大气压强：{pressure}, 空气质量等级：{air_level}。\n"
		  f"根据今日空气质量，建议您{air_tips}")
	if alert:
		print(f'最后，是关于本日的天气预警：{alert}')
	# print(res_json)
	# print(weather)


if __name__ == '__main__':
	weather()
						



		
