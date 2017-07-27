def loop(x,step):
    numbers = []
    i = 0
    #while i < x:
    for i in range(0,6):
        print("At the top i is %d" %i)
        numbers.append(i)
      #  i = i + step
        print("Number now:",numbers)
        print("At the bottom i is %d" %i)
    return numbers

numbers = loop(6,1)
print("The numbers:")
for num in numbers:
	print(num)