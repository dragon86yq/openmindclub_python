def caculate(x,y):
    sum = x + y
    substruct = x - y
    multiply = x * y
    divide = x / y
    print("sum is : %f\nsubstruct is : %f\nmultiply is : %f\ndivide is : %f" % (sum,substruct,multiply,divide))

print ("We can just give the function numbers directly:")
caculate(10,5)

print ("OR, we can use variables from our script:")
x = 20
y = 2
caculate(x,y)

print ("We can even do math inside too:")
caculate(20 + 20, 2 + 2)

print ("And we can combine the two, variables and math:")
caculate(x + 22, y + 4)

first_data = input("input first data")
secodn_data = input("input second data")
first_data = float(first_data)
secodn_data = float(secodn_data)
print ("And we can use variables from keyboard:")
caculate(first_data,secodn_data)

print ("And we can combine the two , variables from the keyboard and math:")
caculate(first_data + 10,secodn_data + 5)

print ("And we can combine the two  variables :")
caculate(first_data + x,secodn_data + y)






