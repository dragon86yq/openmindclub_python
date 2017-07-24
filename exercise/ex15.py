# 从系统导入参数argv
from sys import argv
# 一共导入2个参数，分别赋值给script, filename
script, filename = argv
# 打开一个指定文档，将返回值赋值给参数txt
txt = open(filename)
# 打印文件名字
print("Here's your file %r :"%filename)
# 打印对应文件中的内容
print (txt.read())
# 打印信息
print ("Type the filename again:")
# 输入另外一个文件名字
file_again = input(">")
# 打开上面输入的文件
txt_again = open(file_again)
# 将文件中的内容读出来
print(txt_again.read())