import math

file = open("data.txt", "r")
data_list = file.readlines()
total_fuel = 0
for data in data_list:
    mass = int(data)
    fuel = math.floor((mass / 3)) -2
    total_fuel += fuel

print(total_fuel)
