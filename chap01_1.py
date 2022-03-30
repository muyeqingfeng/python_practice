#  Name : muyeqingfeng
# E-mail: muyeqingfeng@126.com

"""
2020年的新冠病毒给全人类带来了灾难，现在向简单对疫情传播模型进行推测，从而预知病毒的扩散速度。
假设：病毒平均每5天1个人即传染给2个人，如果不加人为控制，预测在第31天、61天的感染人数
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

if __name__ == '__main__':
	people_31 = viral_communication_speed(31)
	people_61 = viral_communication_speed(61)
	print('第31天感染人数为：{0}；\n第61天感染人数为：{1}；' \
	      .format(people_31, people_61))
