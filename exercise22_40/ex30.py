# 设置变量
people = 20
cats = 30
dogs = 15

# 判断people和cats大小关系，如果people小于cats执行if下面语句
if people < cats:
	print("Too many cats! The world is doomed!")
#如果people大于cats执行elif下面语句
elif people > cats:
	print("Not many cats! The world is saved!")
else:
	print("We can't decide.")
	
if people < dogs:
	print("The world is drooled on!")
elif people > dogs:
	print("The world is dry!")
else:
	print("We can't decide 1.")
