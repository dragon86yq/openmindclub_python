### 学习笔记
**ex1**：
python 2使用print ""；python3 使用print ("")。

**ex2**：
“#”能够对代码进行注释，解释下面执行的代码的功能。

**ex3**：
print函数能够打印""里面的信息，也能够打印数学公式计算出来的结果。

**ex4**：
可以将一个数值赋值给一个参数，以后如果使用到这个数值时，直接调用参数即可。

**ex5**：
-  print()函数可以打印不同类型的变量：字符或数字，同时还能够对输出结果进行对齐，确定打印出来的变量的长度和精度；
-  将同一个数字或字符串赋值给不同的变量，使用变量打印出来的结果是相同的。


**ex6**：
-  在strng中可以有string存在；
-  + 可以连接2个sting。


**ex8**：
-  %r 能够打印出 %()后面原始的数据。
-  如果string中有单引号存在，那么打印出来的结果会使用双引号。



**ex9**：
- 使用\n时能够自动换行。
- \（反斜杠），用于转义字符

**ex10**：
- 使用/s和/r打印出来的结果不一样。使用/s直接打印出双引号中的内容，使用/r将双引号中的内容使用单引号显示出来。
- 常用的转义字符
```
\\         Backslash(\)
\'         Single-quote(')
\''        Double-quote('')
\a        ASCII bell(BEL)
\b        ASCII backspace(BS)
\f         ASCII formfeed(FF)
\n        ASCII linefeed(LF)
\N
\r        ASCII
\t        ASCII
\uxx
\v
```

**ex11**：
- 使用input()函数，能够通过交互界面输入一个参数。

**ex12**：
-  使用python -m pydoc input 能够查看builtin函数input()的用法；
-  在python3.6 IDLE中运行python -m pydoc input出现错误如下：
  SyntaxError: invalid syntax。解决方法：查询资料后知道，需要在windows下cmd窗口运行python -m pydoc input才能够正常显示出信息。
-  还可以使用help(input())或者dir(input())，查看函数信息。

**ex13**：
- 直接运行ex13.py时，报错如下：
```
H:\python\exercise>python ex13.py
Traceback (most recent call last):
  File "ex13.py", line 2, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)
```
阅读错误后发现是变量不够，重新阅读之后发现正确的运行方式是python ex13.py 1 2 3，在运行文件之后需要有3个参数，程序才能够正常运行。
- argv是要给数组的参数，默认只有一个参数argv[0]，要增加参数需要在运行.py时 设置参数。
- 在练习study drill时，将输入变量中间加入“,” ，出现如下错误
```
H:\python\exercise>python ex13_2.py hubei , wuhan , jiangan 185123456789
Traceback (most recent call last):
  File "ex13_2.py", line 2, in <module>
    script, province, city, street, phone = argv
ValueError: too many values to unpack (expected 5)
```
解决：在运行.py程序时，变量之间不能有符号，系统会把符号当成变量。
- WYSS means what you should see


**ex14**：
- 在input()函数中可以输入一些提示信息便于告之输入者需要输入信息的类型。

**ex15**：
- 运行ex15.py时出现错误如下：
```
H:\python\exercise>python ex15.py ex15_sample.txt
Traceback (most recent call last):
  File "ex15.py", line 3, in <module>
    txt = open(filename)
FileNotFoundError: [Errno 2] No such file or directory: 'ex15_sample.txt'
```
阅读错误信息后，发现是因为在目录中没有ex15_sample.txt存在，在目录中新建ex15_sample.txt之后，可以正常运行。
-  open()函数返回一个file object。如果不能够打开文件，会返回一个OSError的错误。
-  open()函数可以选择如下方式打开一个文件：
```
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of the file if it exists
'b' binary mode
't' text mode (default)
'+' open a disk file for updating (reading and writing)
'U' universal newlines mode (deprecated)
```
- read()函数能够一次读取文件的全部内容，与read()类似的函数有readline()和readlines()。readline()一次读取一行数据，readlines()一次读取全部数据。

**ex16**：
- truncate()函数用于截断文件，如果指定了可选参数size，则表示截断文件为size个字符。如果没有指定size，则从当前位置起截断；截断之后size后面的所有字符被删除。
- write()函数既可以一行一行的写，也可以一次全部写入。


**ex17**：
- input()函数不进行赋值时，输入回车继续往下执行，输入Ctrl+C结束程序。
- exists()函数检查文件是否存在，如果文件存在返回True，如果文件不存在返回False。
- os模块是python标准库中一个用于访问操作系统功能的模块。
- linux下cat 命令可以查看文件内容；windows下type命令可以查看文件内容。


**ex18**：
- function的作用：写一个function后，下次需要使用时，能够直接调用该function，而不需要重新写一次代码。
- function以def关键词开头，后面接函数标识符名称和圆括号()。
- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定于参数。
- 函数内容以冒号开始，并且缩进；函数可以带return ，也可以不带return。
- 调用函数时，直接调用函数名并赋值参数即可实现函数的功能。
- 函数checklist：
```
1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you “end” your function by going back to writing with no indent (dedenting we call it)?
And when you run (“use” or “call”) a function, check these things:
1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?
```

**ex19**：
- 在做study drill时出现如下错误:
```
And we can use variables from keyboard:
Traceback (most recent call last):
  File "ex19_1.py", line 25, in <module>
    caculate(first_data,secodn_data)
  File "ex19_1.py", line 3, in caculate
    substruct = x - y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```
解决方法：input()函数输出的数据类型是str，需要将str转换为float

**ex20**：
- seek()方法用于移动文件读取指针到指定位置。
    * 语法如下：fileObject.seek(offset[, whence])
    * 参数：offset —— 开始的偏移量，也就是代表需要移动偏移的字节数；whence : 可选，默认值为0。0表示从文件开头开始算起；1表示从文件当前位置算起；2代表从文件末尾算起。
- current_line += 1 means current_line =  current_line + 1



**ex24**：
1. 查看python路径的方法
import sys
print(sys.path) / print(sys.excutable)


**ex25**:
1. 当执行的.py文件不在默认运行目录中时，需要添加.py所在目录，方法如下：
sys.path.append("h://python//exercise//ex24_43")
sys.path.insert(0, 'h:/python/exercise/ex24_43')  
2. 函数split用法
    - split：通过指定分隔符对字符串进行切片，如果参数num有指定值，仅分割num次
    - 语法：str.split(str="", num = string.count(str))
    - 参数： str -- 分隔符，某人为所有空字符，包括空格、换行、制表符等；num -- 分割次数
    - 返回值：返回分割后的字符串

**ex26**:
1.出现错误时需要仔细阅读错误代码，并且在错误指定行上下查看是否有错误。

**29**:
1. :说明下面会有一个新的模块。
2. 4个空格表示新模块的内容是什么。


**ex32**:
1. for的用法：for循环可以遍历任何序列的项目，如一个列表或者一个字符串
    - 语法： for iterating_var in sequence:
                       statements
2. list中append()的用法：
3. list相关操作：
    - 列表可以进行的操作包括索引、切片、加、乘、检查成员。
    - 列表的数据不需要具有相同类型。
    - 列表索引从0开始。
    - 列表相关操作：
        - 在列表末尾添加新对象append()
        - 删除列表元素del()
        - 比较两个列表的元素cmp(list1,list2)
        - 列表元素个数len(list)
        - 返回列表最大值max(list)
        - 返回列表最小值min(list)
        - 将元组转换为列表list(seq)
        - 统计某个元素在列表中出现的次数count(obj)
        - 在列表中找出某个值第一个匹配项的索引位置index(obj)
        - 将对象插入列表insert(index,obj)
        - 移除列表中的一个元素pop(obj)
        - 移除列表中某个值的第一个匹配项remove(obj)
        - 反向列表元素reverse()
        - 对原列表进行排序sort()
    - 列表对+和*的操作符与字符串相似，+号用于组合列表，*号用于重复列表。
    参考：[列表](https://www.runoob.com/python/python-strings.html)

**ex35**:
1. exit(0)能够终止程序

**ex38**:
1. join方法
    - 用于将序列中的元素以制定的字符连接生成一个新的字符串。
    - 语法：str.join(sequence)，sequence要连接的字符串。
    - 返回值：返回通过制定字符连接序列中元素后生成的新字符串


**ex39**:
1. 字典使用键值(key => value)，每个键值用冒号(:)分割，每个对之间用逗号(,)分割，整个字典用花括号{}。
2. 访问字典中的元素可以把相应的键放入方括号[]
3. del可以删除字典中的元素
4. 字典包含的内置方法：
    - 删除字典内所有元素clear()。
    - 返回一个字典的浅复制copy()。
    - 返回制定键的指，如果值不在字典返回default值get(key,default)
    - 以列表返回可编列的（键，值）元组数组items()
    - 以列表返回一个字典所有的键keys()
    -  以列表返回一个字典所有的值values()
参考：[字典](http://www.runoob.com/python/python-dictionary.html)

**40**:
0. class后面紧接着是类名，类名通常是大写开头单词，紧接着是(object)，表示该类是从哪个类继承下来的。通过，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
1. OPP最重要的概念是类(Class)和实例(Instance)。
2. 类是抽象的，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
3. 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把参数等属性绑上去。
4. __init__方法的第一个参数永远是**self**，表示**创建的实例本身**，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向**创建的实例本身**。
5. 有了__init__方法，在创建实例的时候，就不能传入空的参数，必须传入与__init__方法匹配的参数，但是self不需要传，Python解释器自己会把实例变量传进去。
6. 要定义一个方法，除了第一个参数是self外，其他的和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入。
参考：[面向对象编程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000)
