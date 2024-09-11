# 在 Python 中，文件操作是一个非常常见且重要的任务，涵盖了文本文件、二进制文件的读写以及文件系统操作。下面是对文件操作的系统介绍：
#
# 1. 文本文件的读写
# Python 提供了内置的 open() 函数来打开文件。常用的模式包括：
#
# 'r'：只读模式（默认模式）
# 'w'：写入模式（会覆盖文件）
# 'a'：追加模式（在文件末尾添加内容）
# 'r+'：读写模式
# 示例：文本文件的读写
# 写入文本文件
import os
current_dir = os.getcwd()
print(current_dir)
new_path = os.path.join('E:\Python\my-first-repository\Self_study_python', 'txt')
print(new_path) # 拼接路径
if not os.path.exists(new_path):
    os.makedirs(new_path)
txt_path = os.path.join(new_path, 'example.txt')
with open(txt_path, 'w') as f:
    f.write("Hello, Python!\n")
    f.write("This is a new file.\n")
# 读取文本文件
with open(txt_path, 'r') as f:
    content = f.read()
    print(content)
# 常见操作：
# read()：读取整个文件
# readline()：读取一行
# readlines()：将文件内容按行返回为一个列表
# write()：写入字符串
# writelines()：将多个字符串写入文件
# 2. 二进制文件的读写
# 对于二进制文件（如图像、音频文件），需要以 'rb' 或 'wb' 模式打开，分别表示二进制读和写。
# 示例：二进制文件的读写
# 写入二进制文件
data = b'\x00\x01\x02\x03\x04\x05'
with open('binary_file.bin', 'wb') as f:
    f.write(data)
# 读取二进制文件
with open('binary_file.bin', 'rb') as f:
    binary_data = f.read()
    print(binary_data)


# 4. 上下文管理器
# 使用 with 语句可以确保在使用完文件后自动关闭文件，避免资源泄漏。
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
# 文件会自动关闭
# 读取大文件
# 处理大文件时，可以使用 readline() 或者迭代器按行读取，避免将整个文件加载到内存中。
# 示例：按行读取大文件
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())