# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp" :
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# data_dict = {
#     "Fur Color" : ["grey", "red", "black"],
#     "Count" : [2473, 392, 103]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrel)
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
