#  Name : muyeqingfeng
# E-mail: muyeqingfeng@126.com

"""
在实验一的基础上，现在准备模拟医院打响疫情阻击战的过程。随着疫情发生，病毒专家发现
人被病毒感染后，有约14天的潜伏期，也就是这期间感染者没有任何一样，第14天感染征兆
发生，如干咳、高烧、胸闷、无力，患者开始去医院医治。医院对入院病人的平均救治时间为
10天，也就是入院10天后治愈可以出院。这里设定医院累积出院超过1000人时（可以假设
医院人数饱和），日均出院人数为1000人，求第31天、61天的出院人数。
"""

def viral_communication_speed(etime, num=1):
	"""
	病毒 传播 速度
	num: 开始病毒感染人数
	dtime: 第 dtime 天
	"""
	dtime = 0  #间隔时间
	stime = 0  #初始化时间
	people = [num] #感染人数

	while dtime < etime:
		dtime += 1
		if (dtime - stime) % 5 == 0:
			num = 2*num + num
			people.append(num)
		else:
			num = num
			people.append(num)

	return people[-1]

def discharged_number(etime):
	"""
	出院人数：感染后14天入院，10天后治愈
	即：感染后24天能出院
	"""
	num = []
	if etime < 24:
		num0 = 0
		num.append(num0)
	else:
		num0 = viral_communication_speed(etime-23, num=1)
		if num0 <= 1000:
			num.append(num0)
		else:
			num.append(1000)
	return num

if __name__ == '__main__':
	num_31 = discharged_number(31)
	num_61 = discharged_number(61)
	print('第31天出院人数为：{0}；\n第61天出院人数为：{1}'.format(num_31, num_61))