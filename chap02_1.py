#  Name : muyeqingfeng
# E-mail: muyeqingfeng@126.com

"""
实验一：修改2.3节案例9代码，用从reduce=2开始增1的方法求两个整数的最大公约数，要求循环次数最优。
"""

def Divisor(x,y):
	reduce = 2
	if min(x,y) == 1 or x==y:
		return min(x,y)
	elif x<y:
		reduce = x
	else:
		reduce = y

	if x%reduce == 0 and y%reduce == 0:
		return reduce
	else:
		reduce -= 1


try:
	a = int(input('输入第一个整数：'))
	b = int(input('输入第二个整数：'))
	if a <= 0 or b <= 0:
		print('输入的整数应该大于0')
	else:
		print('%d和%d的最大公约数是%d'%(a,b,Divisor(a,b)))
except:
	print('输入数有错！')


