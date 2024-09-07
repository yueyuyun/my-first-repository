# 变量及数据结构
# Python 支持多种基本数据类型，常见包括字符串、整数、浮点数、布尔值、列表、元组、字典、集合等。
# 内置函数
# len(): 返回数据的长度，如字符串、列表、字典等。
# max() 和 min(): 返回最大值和最小值。
# sum(): 返回数值序列的和。
# sorted(): 返回排序后的列表


# 2.1 字符串（str）
# 字符串用于表示文本，它由一对单引号或双引号括起来。

s = "hello"
print(s[0])  # 访问字符串的第一个字符：h
print(s[-1])  # 访问最后一个字符：o
print(s[1:4])  # 切片操作：ell
s = "Python"
print(s.lower())  # 转为小写：python
print(s.upper())  # 转为大写：PYTHON
print(s.replace("P", "J"))  # 替换字符：Jython
print(len(s))  # 计算字符串长度：6

# 2.2 整数（int）和浮点数（float）
# 整数和浮点数是用于数学运算的基本数据类型。

a = 10  # 整数
b = 3.14  # 浮点数

# 运算
sum_ = a + b  # 加法：13.14
diff = a - b  # 减法：6.86
product = a * b  # 乘法：31.4
quotient = a / b  # 除法：3.184713375796178
int_div = a // b  # 整数除法：3
modulus = a % b  # 取余：2.72

# 2.3 列表（list）[]
# 列表是 Python 中非常常用的数据类型，可以存储一组有序的元素，元素可以是不同类型的数据。


lst = [1, 2, 3, 4, 5]
print(lst[0])  # 访问第一个元素：1
print(lst[-1])  # 访问最后一个元素：5
print(lst[1:4])  # 切片操作：[2, 3, 4]

# 列表修改
lst.append(6)  # 添加元素：lst = [1, 2, 3, 4, 5, 6]
lst.remove(2)  # 删除元素：lst = [1, 3, 4, 5, 6]
lst[0] = 0  # 修改元素：lst = [0, 3, 4, 5, 6]

lst = [1, 2, 3, 2, 4]
print(len(lst))  # 列表长度：5
print(lst.count(4))  # 统计某元素出现次数：2
lst.reverse()  # 列表反转：[4, 2, 3, 2, 1]
print(lst)
# 2.4 字典（dict）{}
# 字典是键值对的无序集合，键是唯一的，而值可以重复。

d = {"name": "Alice", "age": 25}
print(d["name"])  # 访问键为"name"的值：Alice
d["age"] = 26  # 修改字典中的值
d["gender"] = "Female"  # 添加新键值对
print(d)
d = {"name": "Alice", "age": 25}
print(d.keys())  # 获取所有键：dict_keys(['name', 'age'])唯一
print(d.values())  # 获取所有值：dict_values(['Alice', 25])
print(d.items())  # 获取所有键值对：dict_items([('name', 'Alice'), ('age', 25)])
# 2.5 集合（set）{}
# 集合是无序且不重复的元素集合。
s = {1, 2, 3, 3}
print(s)  # 集合自动去重：{1, 2, 3}

s.add(4)  # 添加元素：{1, 2, 3, 4}
s.remove(1)  # 删除元素：{2, 3, 4}

# 2.6 元组（tuple）（）
# 元组和列表类似，但元组是不可变的，一旦创建，不能修改。

t = (1, 2, 3)
print(t[0])  # 访问第一个元素：1
# t[0] = 0  # 错误操作，元组不可变
# 3. 基础操作与使用技巧
# 3.1 变量的类型转换
# 不同类型的数据可以通过内置函数进行转换。
a = "123"
b = int(a)  # 字符串转整数
c = float(b)  # 整数转浮点数
print(b)
print(c)
# 3.2 判断数据类型
# 使用 type() 函数可以判断变量的数据类型。
x = 5
print(type(x))  # 输出：<class 'int'>
print(type(a))
print(type(c))
# 3.3 条件与循环
# Python 中条件语句和循环是控制程序流程的重要部分。
#
# 条件判断：
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
# for 循环
for i in range(5):
    print(i)  # 输出：0 1 2 3 4

# while 循环
x = 0
while x < 5:
    print(x)
    x += 1  # 每次循环后加 1