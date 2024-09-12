import os
import math
# 在Python中，异常处理是确保代码在遇到错误时能够优雅处理而不崩溃的重要机制。下面是关于异常处理的一些系统性知识：
# 1. 基础异常处理 - try-except 语句
# try-except 用来捕获并处理代码中的异常，防止程序因错误而终止。
# 基本结构：
# try:
#     # 可能抛出异常的代码
# except ExceptionType as e:
#     # 异常处理代码
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")
# 2. else 和 finally 语句
# else：如果 try 中的代码没有抛出异常，则执行 else 代码。
# finally：无论是否有异常，finally 中的代码都会执行，常用于释放资源或清理操作。
try:
    x = 10 / 2
except ZeroDivisionError:
    print("除以0的错误")
else:
    print("没有异常发生")
finally:
    print("无论如何都会执行")

# 3. 捕获多种异常
# 可以通过捕获多个异常类型来处理不同的错误。
try:
    x = int("abc")  # 这将引发 ValueError
except (ValueError, ZeroDivisionError) as e:
    print(f"捕获到异常: {e}")
# 自定义异常类
# 在实际项目中，可能需要根据特定需求创建自定义的异常类。这通常继承自内置的 Exception 类。
# 自定义异常类：
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print(f"捕获到自定义异常: {e.message}")

# # raise 用于主动引发异常，可以抛出内置异常或自定义异常。
# try:
#     raise ValueError("手动引发的异常")
# except ValueError as e:
#     print(f"捕获到异常: {e}")
# # 使用上下文管理器来简化异常处理
# # 对于一些特定场景，Python 提供了上下文管理器（例如文件操作）来自动处理资源的释放和异常处理。
# with open("file.txt", "r") as f:
#     data = f.read()
# # 不需要显式的 try-finally 来关闭文件
# 1. Exception
# 这是所有异常类的基类。通常情况下，你会捕获具体的异常类型，而不是直接捕获 Exception。
try:
    raise Exception("这是一个通用异常")
except Exception as e:
    print(f"捕获到异常: {e}")
# 2. ArithmeticError
# 这是所有算术运算异常的基类，包括以下几个子类：
# ZeroDivisionError：当尝试除以零时抛出。
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"捕获到除以0的异常: {e}")
# OverflowError：当数值运算结果超过表达范围时抛出，通常出现在浮点数计算中。
try:
    math.exp(1000)  # 指数过大，导致溢出
except OverflowError as e:
    print(f"捕获到溢出错误: {e}")
# FloatingPointError：在浮点运算发生错误时抛出（较少遇到）。
# 3. LookupError
# 所有查找操作失败时的基类，包括以下两个常见子类：
# IndexError：访问列表、元组等序列中不存在的索引时抛出。
try:
    lst = [1, 2, 3]
    print(lst[5])  # 无效索引
except IndexError as e:
    print(f"捕获到索引错误: {e}")
# KeyError：在字典中访问不存在的键时抛出。
try:
    d = {'a': 1}
    print(d['b'])  # 'b' 键不存在
except KeyError as e:
    print(f"捕获到键错误: {e}")
# 4. ValueError
# 当函数接收到的参数类型正确但值不合适时抛出，例如将非整数字符串转换为整数。
try:
    x = int("abc")  # 不能将字符串转换为整数
except ValueError as e:
    print(f"捕获到值错误: {e}")
# 5. TypeError
# 当操作或函数应用于不适合的对象类型时抛出。
try:
    x = 'abc' + 123  # 字符串和整数不能相加
except TypeError as e:
    print(f"捕获到类型错误: {e}")
# 6. AttributeError
# 当访问的属性不存在时抛出。
try:
    class MyClass:
        pass

    obj = MyClass()
    obj.some_attribute  # 访问不存在的属性
except AttributeError as e:
    print(f"捕获到属性错误: {e}")
# 7. ImportError 和 ModuleNotFoundError
# ImportError：在导入模块时出错时抛出（无法找到模块或模块加载失败）。
# ModuleNotFoundError：是 ImportError 的一个子类，当指定模块不存在时抛出。
try:
    import non_existent_module  # 模块不存在
except ModuleNotFoundError as e:
    print(f"捕获到模块未找到错误: {e}")
# 8. FileNotFoundError
# 当尝试打开不存在的文件时抛出。
try:
    with open("non_existent_file.txt", "r") as f:
        pass
except FileNotFoundError as e:
    print(f"捕获到文件未找到错误: {e}")
# 9. IOError
# 这是 I/O 操作失败时抛出的异常，包括文件操作错误、设备不可用等。现代 Python 中 IOError 通常与 OSError 结合在一起。
try:
    with open("non_existent_file.txt", "r") as f:
        pass
except IOError as e:
    print(f"捕获到I/O错误: {e}")
# 10. AssertionError
# 当使用 assert 语句时，断言条件为 False 时抛出。
try:
    assert 1 == 2, "这不是一个正确的断言"
except AssertionError as e:
    print(f"捕获到断言错误: {e}")
# 11. StopIteration
# 在迭代器没有更多项时抛出，通常在使用 next() 函数时遇到。
try:
    lst = iter([1, 2])
    next(lst)
    next(lst)
    next(lst)  # 没有更多的元素
except StopIteration as e:
    print(f"捕获到停止迭代异常: {e}")
# 12. KeyboardInterrupt
# 当用户按下 Ctrl+C 或中断程序执行时抛出。

try:
    while True:
        pass
except KeyboardInterrupt as e:
    print(f"捕获到键盘中断: {e}")
# 13. MemoryError
# 当程序内存不足时抛出。
try:
    large_list = [1] * (10**10)  # 超过内存限制
except MemoryError as e:
    print(f"捕获到内存错误: {e}")


# 14. RuntimeError
# 这是一个通用异常，表示检测到无效的运行时状态。通常出现在不明确的错误场景。
try:
    raise RuntimeError("这是一个运行时错误")
except RuntimeError as e:
    print(f"捕获到运行时错误: {e}")
# 15. OSError
# 当系统函数返回与系统相关的错误时抛出，例如文件系统错误、网络错误等。
try:
    os.remove("non_existent_file.txt")  # 删除不存在的文件
except OSError as e:
    print(f"捕获到操作系统错误: {e}")