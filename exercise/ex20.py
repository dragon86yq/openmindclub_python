# 从系统导入argv参数
from sys import argv
# argv参数赋值给变量script、input_file
script ,input_file = argv
# 定义函数print_all，功能是：读取参数f的所有内容
def print_all(f):
    print(f.read())
# 定义函数rewind，功能是：将文件指针指向文件头
def rewind(f):
    f.seek(0)
# 定义函数print_a_line，功能是：读取参数f制定位置line_count的一行数据
def print_a_line(line_count,f):
    print(line_count,f.readline())

# 打开制定文件input_file
current_file = open(input_file)

print("First let's print the whole file :\n")

# 调用函数print_all，打印出current_file中全部内容
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# 调用函数rewind，让current_file指向文件头位置
rewind(current_file)

print("Let's print three lines:")

# 变量current_line加1，current_line = 1
current_line = 1
print(current_file)
#调用函数print_a_line，打印指定行current_file的内容
print_a_line(current_file,current_file)
# 变量current_line加1,current_line = 2
current_line = current_line + 1
#调用函数print_a_line，打印指定行current_file的内容
print_a_line(current_file,current_file)
# 变量current_line加1,current_line = 3
current_line = current_line + 1
#调用函数print_a_line，打印指定行current_file的内容
print_a_line(current_file,current_file)







