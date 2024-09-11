import itertools
# # 条件与循环
# # Python 中条件语句和循环是控制程序流程的重要部分。
# #
# # 条件判断：
# x = 10
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is 5")
# else:
#     print("x is less than 5")
# # for 循环
# for i in range(5):
#     print(i)  # 输出：0 1 2 3 4
# # while 循环
# x = 0
# while x < 5:
#     print(x)
#     x += 1  # 每次循环后加 1
# 在 Python 中，for 循环不仅用于简单的迭代，还可以与其他高级特性结合使用，形成高阶用法。这些高级 for 循环能让代码更加简洁、高效，但有时也更难理解。下面我介绍几种常见的高阶 for 循环技巧。

# 1. 列表推导式（List Comprehension）
# 列表推导式是一种简洁的语法，用于从一个可迭代对象生成一个新列表。
# 普通 for 循环实现
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)
# 列表推导式实现
squares = [i ** 2 for i in range(10)]
print(squares)
# 列表推导式可以在一行代码中生成列表，常用于对列表进行过滤和转换。
# 带条件的列表推导式：
# 只生成偶数的平方
even_squares = [i ** 2 for i in range(20) if i % 2 == 0]
print(even_squares)

# 使用 for 循环生成字典
squares = {}
for i in range(5):
    squares[i] = i ** 2
print(squares)
# 字典推导式实现
squares = {i: i ** 2 for i in range(5)}
print(squares)
squares = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(squares)

# 3. 集合推导式（Set Comprehension）
# 与列表和字典类似，集合推导式用于生成集合（不包含重复值）。
# 示例：
# 生成一个包含所有偶数的集合
evens = {i ** 3 for i in range(5) if i % 2 == 0}
print(evens)

# 4. 生成器表达式（Generator Expression）
# 生成器表达式类似于列表推导式，但它不会一次性生成整个列表，而是每次请求一个值时才生成，可以节省内存。
# 生成器表达式
gen = (i ** 2 for i in range(10))
print(gen)
# 逐个获取值
for val in gen:
    print(val)
# 5. 嵌套 for 循环
# 在推导式中，允许使用嵌套的 for 循环
# 普通嵌套循环
pairs = []
for i in range(3):
    for j in range(2):
        pairs.append((i, j))
print(pairs)
# 嵌套的列表推导式
pairs = [(i, j) for i in range(3) for j in range(2)]
print(pairs)
# 6. 高阶函数与 map()、filter() 函数
# 6. zip() 和 enumerate() 与 for 循环结合
# zip()：用于同时迭代多个可迭代对象。
# enumerate()：用于在遍历列表时同时获取索引和元素。
# zip() 示例
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# enumerate() 示例
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index {index} has value {value}")
# 7. 条件表达式与 for 循环结合
# 条件表达式可以用在循环中，简化代码。
# 带条件的列表推导式
nums = [i if i % 2 == 0 else -i for i in range(10)]
print(nums)  # 输出： [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]
# 8. 嵌套数据结构的迭代
# 对于嵌套数据结构（如二维列表），可以使用嵌套的 for 循环来进行遍历。

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 普通嵌套 for 循环
for row in matrix:
    for value in row:
        print(value)
# 列表推导式遍历二维数组
flattened = [value for row in matrix for value in row]
print(flattened)
# 9. itertools 模块与高级 for 循环
# itertools 是 Python 内置的一个库，提供了一些用于操作迭代器的高级函数。
#
# 常用函数：
# itertools.product()：返回多个可迭代对象的笛卡尔积。
# itertools.permutations()：返回给定序列的所有排列组合。
# itertools.chain()：将多个可迭代对象串联起来进行迭代。

# 笛卡尔积
for pair in itertools.product([1, 2], ['a', 'b']):
    print(pair)
# 排列组合
for perm in itertools.permutations([1, 2, 3]):
    print(perm)
# 10. 解构赋值与 for 循环
# Python 的解构赋值允许你从列表或元组中直接解包多个值。
# 解包元组
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, char in pairs:
    print(num, char)