import numpy as np
import pandas as pd
import time
# NumPy 更适合于数值计算、矩阵操作等任务，常用于科学计算。
# Pandas 则更适合处理结构化的表格数据，特别是在数据清洗、预处理、分析方面表现出色。

# numpy
# 创建一个 2x3 的数组
a = np.array([[1, 2, 3], [4, 5, 6]])

# 数组基本操作
print("数组形状:", a.shape)  # 输出：数组形状: (2, 3)
print("数组元素和:", a.sum())  # 输出：数组元素和: 21

# 数组加法
b = np.array([[1, 1, 1], [2, 2, 2]])
print("数组相加:\n", a + b)
# 数组的元素乘法  matlab中的.*
print("数组元素乘法:\n", a * b)

# 1.1 广播机制（Broadcasting）
# 广播机制允许在不同形状的数组之间执行运算，而无需显式地进行扩展。

# 数组 a 是 2x3, 数组 b 是 1x3
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])
print("数组a形状:", a.shape)
print("数组b形状:", b.shape)
# 广播机制会自动将 b 扩展为与 a 相同的形状，然后进行逐元素运算
result = a + b
print(result)

# 1.2 向量化运算（Vectorization）
# 向量化运算是指避免使用循环的情况下对数组进行操作。通过 NumPy 的内建函数，我们可以更高效地进行运算。
# 数据生成
x = np.random.rand(1000000)
y = np.random.rand(1000000)
z = np.zeros(1000000)

# 普通Python循环
start_time_loop = time.time()
for i in range(1000000):
    z[i] = x[i] + y[i]
end_time_loop = time.time()

# 向量化实现
start_time_vectorized = time.time()
z = x + y
end_time_vectorized = time.time()

# 计算时间
loop_time = end_time_loop - start_time_loop
vectorized_time = end_time_vectorized - start_time_vectorized
# 打印结果
print(f"普通Python循环时间: {loop_time:.6f} 秒")
print(f"向量化实现时间: {vectorized_time:.6f} 秒")

# 1.3 数组切片与索引的高级用法
# NumPy 支持复杂的数组索引与切片，比如布尔索引和花式索引。
# 布尔索引
a = np.array([1, 2, 3, 4, 5, 6])
mask = a > 3
print(a[mask])  # 输出：[4 5 6]
# 花式索引
indices = [0, 2, 4]
print(a[indices])  # 输出：[1 3 5]
# 1.4 数组运算中的高级线性代数操作
# NumPy 提供了丰富的线性代数操作功能，比如矩阵乘法、求逆等。
# 矩阵乘法
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)  # 或者使用 A @ B
print(C)  # 输出：[[19 22], [43 50]]

# 矩阵求逆
A_inv = np.linalg.inv(A)
print(A_inv)
# pandas
# 创建一个简单的 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [90, 85, 95]}

df = pd.DataFrame(data)

# 查看 DataFrame
print(df)

# 数据选择与操作
print("查看'Name'列:\n", df['Name'])

# 根据条件筛选数据
print("筛选年龄大于 30 的行:\n", df[df['Age'] >=30])

# 添加一列新数据
df['Passed'] = df['Score'] > 80
print("添加新列后的 DataFrame:\n", df)

# 计算统计量
print("平均年龄:", df['Age'].mean())

# 2.1 GroupBy 与聚合操作
# Pandas 的 groupby 函数可以根据某个（或多个）列对数据进行分组，之后进行聚合操作（如求和、均值等）。

data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Values': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

# 按照 Category 分组，并计算每组的均值
grouped = df.groupby('Category').mean()
# grouped = df.groupby('Category')
print(grouped)

# 2.2 多重索引（MultiIndex）
# Pandas 提供了多重索引，适合处理多维度的数据。
arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Subcategory'))

df = pd.DataFrame({'Values': [10, 20, 30, 40]}, index=index)
print(df)

# 通过索引访问数据
print(df.loc['A'])  # 输出 Category A 下的所有子类
# 2.3 数据透视表（Pivot Table）
# 数据透视表在数据分析中非常有用，它可以通过多种方式对数据进行聚合和重新排列。
data = {'Category': ['A', 'A', 'B', 'B'],
        'Subcategory': ['X', 'Y', 'X', 'Y'],
        'Values': [10, 15, 20, 25]}

df = pd.DataFrame(data)
# 通过透视表聚合数据
pivot_table = pd.pivot_table(df, values='Values', index='Category', columns='Subcategory', aggfunc=np.sum)
print(pivot_table)

# 2.4 应用函数（apply、applymap）
# Pandas 的 apply 函数可以将任意函数应用到 DataFrame 或 Series 的行或列上，applymap 可以应用到每个元素上。
# 应用到整个列
df['Values'] = df['Values'].apply(lambda x: x * 2)
print(df)

# 对整个 DataFrame 的每个元素应用函数
df = df.applymap(lambda x: x if isinstance(x, int) else x.upper())
print(df)
# 2.5 时间序列处理
# Pandas 对时间序列数据处理有着非常强大的支持。它能对时间索引进行操作，如重采样、滚动计算等。
# 创建时间序列
dates = pd.date_range('20230101', periods=31)
df = pd.DataFrame(np.random.randn(31, 4), index=dates, columns=list('ABCD'))
print(df)
# 重采样：按月聚合数据
monthly = df.resample('M').sum()
print(monthly)