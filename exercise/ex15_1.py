from sys import argv
# 一共导入2个参数，分别赋值给script, filename
script, filename = argv
print ("Type the filename again:")
# 输入另外一个文件名字
file_again = input(">")
# 打开上面输入的文件
txt_again = open(file_again)
# 将文件中的内容读出来
print(txt_again.read())