# 定义变量存储个人信息：姓名（字符串）、年龄（整数）、是否已婚（布尔值），并打印变量类型。

name= '张三'
age= 19
is_merry= True;

print(type(name))
print(type(age))
print(type(is_merry))

#计算圆的面积（公式：面积=π×半径²，π 取 3.14，半径由变量r存储）。


n=3.14
r=int(input('请输入半径'))
square=n*(r**2)
print(square)


#编写程序判断一个数是否为偶数：  输入一个整数num，如果是偶数，打印{num}是偶数；否则打印{num}是奇数。

num=int(input('请输入一个整数'))
if num % 2 == 0 :
    print(f'{num}是偶数')
else:
    print(f'{num}是奇数')


#用for循环打印 1-20 之间的所有奇数。


for i in range(1,21,2):
print(i)


#用while循环计算 10 的阶乘（10! = 10×9×8×…×1）。

