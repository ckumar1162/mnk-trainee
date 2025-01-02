# with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day25_code\weather_data.csv") as fp:
#     data = fp.readlines()
#     print(data)

# import csv
# with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day25_code\weather_data.csv") as fp:
#     data = csv.reader(fp)
#     temp =[]
#     for i in data:
        
#         integers = i[1]
#         if integers != "temp":
#             temp.append(int(integers))
#     print(temp)
#     for i in data:
#         print(i)

import pandas as pd

data = pd.read_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day25_code\weather_data.csv")
# print(data)
# print(data["temp"])
# print(data["temp"].max())
# print(data[data["temp"] == data["temp"].max()])
mon = data[data.day == "Monday"]
f = (mon.temp * 1.8) +32
print(f)