from turtle import Turtle


a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a,b],reverse=True)

print('按照a<=b进行排序，排序结果为：{}，{}'.format(a,b))

