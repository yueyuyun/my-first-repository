import numpy as np
import matplotlib.pyplot as plt#它提供类似 MATLAB 风格的绘图接口图形窗口
import seaborn as sns
import matplotlib.animation as animation#动图
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.font_manager as fm
# plt.ioff()  # 关闭交互模式
#精度评价
# 设置字体为SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体Microsoft YaHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 生成模拟数据
np.random.seed(0)
x = np.random.rand(100, 1) * 10  # 生成100个0到10之间的随机数
y = 2.5 * x + np.random.randn(100, 1) * 2  # 线性关系，加一些噪声

# 拟合线性回归模型
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# 计算精度指标
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)  # 计算均方根误差
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# 绘制图形
plt.figure(figsize=(10, 6))  # 设置图形大小
plt.scatter(x, y, color='blue', label='真实数据', alpha=0.7)  # 绘制散点图
# plt.plot(x, y_pred, color='red', label=f'拟合直线: y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}', linewidth=2)  # 绘制拟合直线
# 绘制拟合直线（不需要在图例中显示方程）
plt.plot(x, y_pred, color='red',label=f'拟合直线', linewidth=2)

# 在图中添加文本
textstr = '\n'.join((
    f'拟合直线方程: y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}',
    f'均方误差 (MSE): {mse:.4f}',
    f'均方根误差 (RMSE): {rmse:.4f}',
    f'平均绝对误差 (MAE): {mae:.4f}',
    f'决定系数 (R²): {r2:.4f}'
))
plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# 设置图形标题和轴标签（包含中文）
plt.title('模拟数据与拟合直线', fontsize=16)  # 设置标题
plt.xlabel('x', fontsize=14)  # 设置x轴标签
plt.ylabel('y', fontsize=14)  # 设置y轴标签
plt.legend(loc='best', fontsize=12)  # 显示图例

# 设置网格线
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)  # 设置网格线样式

# 显示图形
plt.tight_layout()  # 自动调整子图参数，使图形布局紧凑
plt.show(block=False)
plt.savefig('E:\Python\my-first-repository\Self_study_python\图片\精度评价.png', dpi=300, bbox_inches='tight')
bbox_inches='tight' #确保图像边缘不会被裁剪。


# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)
#折线图

plt.figure()
# 画折线图
plt.plot(x, y)
# 添加标题和标签
plt.title('Sine Wave')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# 显示图形
plt.show(block=False)
plt.savefig('E:\Python\my-first-repository\Self_study_python\图片\折线图.png', dpi=300, bbox_inches='tight')
bbox_inches='tight' #确保图像边缘不会被裁剪。


# Seaborn 是基于 Matplotlib 之上的高级绘图库，提供了更高层次的接口，特别适合用于统计图形。
# Seaborn 基础
# 常见图表类型
# 分布图：sns.distplot()，显示数据分布并可以叠加核密度估计（KDE）。
# 箱线图：sns.boxplot()，显示数据的集中趋势及离群点。
# 热力图：sns.heatmap()，用于显示矩阵数据。
# 加载示例数据集
tips = sns.load_dataset("tips")
# 绘制带回归线的散点图
sns.lmplot(x="total_bill", y="tip", data=tips)
# 调色板与主题
# Seaborn 提供了多种预定义的调色板和主题：
sns.set_style("whitegrid")  # 设置背景样式
sns.set_palette("pastel")   # 设置调色板
plt.show(block=False)
plt.savefig('E:\Python\my-first-repository\Self_study_python\图片\带回归线的散点图.png', dpi=300, bbox_inches='tight')
bbox_inches='tight' #确保图像边缘不会被裁剪。


# Pandas 提供了简单的绘图接口，适合直接从数据框中生成图表：
# 创建DataFrame
df = pd.DataFrame({
    'x': x,
    'y': y
})

# 使用DataFrame绘制
df.plot(x='x', y='y', kind='line')
# 基础知识
# 图形（Figure）: 整个绘图区域，包含多张子图，可以通过 plt.figure() 创建。
# 子图（Subplot）: 单张图，可以通过 plt.subplot() 或 plt.subplots() 创建多个子图，分别绘制。
# 轴（Axis）: 图的坐标系，定义 x 轴和 y 轴的范围、刻度和标签。
# 标题、标签和图例: 标题使用 plt.title()，轴标签用 plt.xlabel() 和 plt.ylabel()，图例通过 plt.legend()。
# 常见图表类型
# 折线图（Line Plot）：显示数据的趋势。

plt.plot(x, y)
# 散点图（Scatter Plot）：用于展示变量之间的关系。
plt.scatter(x, y)
# 柱状图（Bar Plot）：用于展示分类数据。
categories = ['A', 'B', 'C']
values = [5, 7, 3]
plt.bar(categories, values)

# 直方图（Histogram）：用于展示数据的分布。
data = np.random.randn(1000)
plt.hist(data, bins=30)
# 饼图（Pie Chart）：显示部分和整体的关系。
plt.pie(values, labels=categories)
# 样式与美化
# 颜色：可以通过 color 参数设置线条和点的颜色，如 'blue', '#FF5733'。
# 线型：通过 linestyle 设置，如 '-'（实线），'--'（虚线）。
# 标记：通过 marker 设置点的形状，如 'o', 's', 'x'。
# 你可以在一张图中绘制多个子图：
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].scatter(x, y)
axs[1, 0].bar(categories, values)
axs[1, 1].hist(data, bins=30)
plt.show(block=False)
# gridspec 允许你更精细地控制子图的排列方式。
plt.savefig('E:\Python\my-first-repository\Self_study_python\图片\子图.png', dpi=300, bbox_inches='tight')
bbox_inches='tight' #确保图像边缘不会被裁剪。


# 动态展示sin函数
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

def update(num, x, line):
    line.set_ydata(np.sin(x + num/10))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, fargs=[x, line])
# 保存动图
ani.save('E:\Python\my-first-repository\Self_study_python\图片\动图.gif', writer='imagemagick', fps=30)
# 如果要保存为 mp4 格式：
# ani.save('path/to/save/sine_wave_animation.mp4', writer='ffmpeg', fps=30)
plt.show(block=False)
