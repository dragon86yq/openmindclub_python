# cars设置为100
cars = 100

# space_in_a_car设置为floatin point 4.0
space_in_a_car = 4.0

# drivers设置为30
drivers = 30

# passengers设置为90
passengers = 90

# cars_not_driven等于cars 减去 drivers
cars_not_driven = cars - drivers

#  cars_driven设置为30
cars_driven = drivers

# carpool_capacity等于cars_driven乘以space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# average_passengers_per_car等于 passengers除以cars_driven
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")


# study drill
# 1.  'average_passengers_per_car = carpool_capacity / passengers'
# NameError : name 'carpool_capacity' is not difined 
# 在前面的语句中灭有定义carpool_capacity信号，或者出carpool_capacity在average_passengers_per_car = carpool_capacity / passengers
# 之前没有出现过。


# 1. use 4 for space_in_a_car
# We can transport 120.0 people today.变成 We can transport 120 people today.
# 2. 4.0 is "floating point"意味着在有参数space_in_a_car = 4.0的计算中，结果将是"floating point"



















