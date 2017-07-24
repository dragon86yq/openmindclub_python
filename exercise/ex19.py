# 定义一个叫做cheese_and_crackers函数，该函数有两个参数cheese_count和boxes_of_crackers
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    # 打印出参数cheese_count是多少
    print ("You have %d cheeses!" % cheese_count)
    # 打印出参数boxes_of_crackers是多少
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    # 打印相关信息
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")

# 打印相关信息
print ("We can just give the function numbers directly:")
# 调用cheese_and_crackers函数，并且参数cheese_count等于20，boxes_of_crackers等于30
cheese_and_crackers(20, 30)

# 打印相关信息
print ("OR, we can use variables from our script:")
# 设变量amount_of_cheese为10，amount_of_crackers为50
amount_of_cheese = 10
amount_of_crackers = 50
# 调用cheese_and_crackers函数，并将上面amount_of_cheese、amount_of_crackers的变量值传入函数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 打印相关信息
print ("We can even do math inside too:")
# 调用cheese_and_crackers函数
# 函数变量amount_of_cheese = 30，amount_of_crackers = 11
cheese_and_crackers(10 + 20, 5 + 6)

# 打印相关信息
# 调用cheese_and_crackers函数
# 函数变量amount_of_cheese = 100 + 10，amount_of_crackers = 50 + 1000
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)