import os
from pathlib import Path
import shutil
# Python 提供了 os 和 shutil 模块来进行文件系统的操作，如文件和目录的创建、删除、重命名等。
#
# 常见的文件系统操作：
# os.path.exists()：检查文件或目录是否存在
# os.remove()：删除文件
# os.rename()：重命名文件
# os.mkdir()：创建目录
# os.rmdir()：删除空目录
# shutil.rmtree()：递归删除目录及其内容

# 获取当前工作目录
# 使用 os 模块
current_dir = os.getcwd()
print(current_dir)
# 使用 pathlib 模块
current_dir = Path.cwd()
print(current_dir)


# 改变当前工作目录
# os.chdir('E:\Python\my-first-repository\Self_study_python\图片')
# current_dir = os.getcwd()
# print(current_dir) # 获取当前工作目录
# # 使用 pathlib 模块
# Path('/path/to/directory').chdir()



# 拼接路径
new_path = os.path.join('E:\Python\my-first-repository\Self_study_python\图片', '子图.png')
print(new_path) # 拼接路径
# 使用 pathlib 模块
new_path = Path(current_dir) / '图片/子图.png'
print(new_path)
paths = {
    'dest_dir': r"测试新建文件夹os",
    'dest_dir2': r"测试新建文件夹pathlib 模块"
        }
# 创建目录
# 确保目标文件夹存在
if not os.path.exists(paths['dest_dir']):
    # 创建文件夹
    os.makedirs(paths['dest_dir'])
    # 使用 pathlib 模块
    Path(paths['dest_dir2']).mkdir(parents=True, exist_ok=True)


# 获取文件名、目录名、文件扩展名
file_name = os.path.basename('my-first-repository/git_commands.docx')
dir_name = os.path.dirname('my-first-repository/git_commands.docx')
file_ext = os.path.splitext('my-first-repository/git_commands.docx')[1]
print(file_name)
print(dir_name)
print(file_ext)
    # 使用 pathlib 模块
path = Path('E:\Python\my-first-repository\git_commands.docx')
file_name = path.name
dir_name = path.parent
file_ext = path.suffix
print(file_name)
print(dir_name)
print(file_ext)

# 递归遍历目录绝对路径
# 使用 os 模块
for root, dirs, files in os.walk('E:\Python\my-first-repository\Self_study_python\图片'):
    print(f"Root: {root}")
    print(f"Dirs: {dirs}")
    print(f"Files: {files}")

# 使用 pathlib 模块
for path in Path('E:\Python\my-first-repository\Self_study_python\图片').rglob('*'):
    print(path)

# 处理相对路径和绝对路径
   # 使用 os 模块
abs_path = os.path.abspath('my-first-repository/git_commands.docx')
print(abs_path)
current_dir = Path.cwd()
print(current_dir)
#    # 使用 pathlib 模块
# abs_path = Path('my-first-repository/git_commands.docx').resolve()
# print(abs_path)

# 删除文件
# os.remove('E:\Python\my-first-repository\Self_study_python\图片\子图.png')
# Path('E:\Python\my-first-repository\Self_study_python\图片\折线图.png').unlink()
# 创建一个空目录
os.makedirs('/mpty_directory', exist_ok=True)
# 检查目录是否为空
if  not os.listdir('/mpty_directory'):
    print("该目录是空目录")

# # 删除空目录
os.rmdir('E:\Python\my-first-repository\Self_study_python\测试新建文件夹os')
Path('E:\Python\my-first-repository\Self_study_python\测试新建文件夹pathlib 模块').rmdir()
#
# # 删除非空目录（用shutil模块）搞不懂
shutil.rmtree('/path/to/directory')
# def delete_output_processed_folder(paths):
#     folder_to_delete = paths['output_processed']
#     if os.path.exists(folder_to_delete):
#         shutil.rmtree(folder_to_delete)
#         print(f"Deleted folder: {folder_to_delete}")
# 复制文件
shutil.copy('/path/to/source.txt', '/path/to/destination.txt')
# # 移动文件或目录
shutil.move('/path/to/source.txt', '/path/to/destination')
# 批量重命名文件
for file in Path('E:\Python\my-first-repository').glob('*.docx'):
    new_name = file.stem + '_new' + file.suffix
    file.rename(file.with_name(new_name))


