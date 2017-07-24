my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)


# study drill

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# 1. %字符：标记转换说明符的开始
# 2. 转换标志：-表示左对齐；+表示在转换值之前要加上正负号；""（空白字符）表示正数之前保留空格；
# 0 表示转换值若位数不够则用0填充
# 3. 点（.）后跟精度值：如果转换的是实数，精度值就表示出现在小数点后的位数。
# 如果转换的是字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元祖中读出。
# 字符串格式转换类型
"""
d,i                 带符号的十进制整数
o                   不带符号的八进制
u                   不带符号的十进制
x                    不带符号的十六进制（小写）
X                   不带符号的十六进制（大写）
e                   科学计数法表示的浮点数（小写）
E                   科学计数法表示的浮点数（大写）
f,F                 十进制浮点数
g                   如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
G                  如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
C                  单字符（接受整数或者单字符字符串）
r                    字符串（使用repr转换任意python对象)
s                   字符串（使用str转换任意python对象）


print("%10.3f" %pi) #字段宽度10，精度3
"""

# inch conver centimeter
centimeter = inch * 2.54














