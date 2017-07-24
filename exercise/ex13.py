from sys import argv
script, first, second, third = argv
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

# study drill
"""
1.直接运行ex13.py时，报错如下：
H:\python\exercise>python ex13.py
Traceback (most recent call last):
  File "ex13.py", line 2, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)
阅读错误后发现是变量不够，重新阅读之后发现正确的运行方式是python ex13.py 1 2 3这样程序才能够正常运行
"""
















