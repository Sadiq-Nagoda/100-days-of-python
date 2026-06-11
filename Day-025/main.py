

# # # with open(os.path.join(base_dir, "weather_data.csv")) as weather_data:
# # #     data = weather_data.readlines()
# # #     print(data)





# # import os
# # import csv


# # base_dir = os.path.dirname(os.path.abspath(__file__))


# # with open(os.path.join(base_dir, "weather_data.csv")) as data_file:
# #         data =  csv.reader(data_file)
# #         temperature = []
# #         for row in data:
# #             if row[1] != "temp":
# #                   temperature.append(int(row[1]))
# #         print(temperature)






# import pandas
# import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
# data = pandas.read_csv(os.path.join(base_dir,"weather_data.csv"))
# # print(data["temp"])


# # data_dict = data.to_dict()
# # print(data_dict)


# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # print(data["temp"].max())

# # #Getting data in columns

# # print(data["condition"])
# # print(data.condition)



# #Getting data in rows

# # print(data[data.day == "Monday"])

# #Max
# # print(data[data.temp == data.temp.max()])




# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32

# # print(monday_temp_F)


# #Create Data frame

# Nagoda_fam = {
#     "childdren": ["mujahid", "sadiq", "safuwa", "abdul", "safwan"],
#     "Age": [21, 19, 16, 14, 10]
# }

# fam = pandas.DataFrame(Nagoda_fam)
# fam.to_csv("Family.csv")

#

import pandas as pd
import os



base_dir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(base_dir,"2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"))
colors = data["Primary Fur Color"]

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)



data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_data")