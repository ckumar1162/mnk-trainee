# with open("weather_data.csv") as f:
#      data=f.readlines()
#      print(data)

# import csv
# with open("weather_data.csv") as f:
#     data=csv.reader(f)
#     temperature=[]
#     for i in data:
#         if i[1]!="temp":
#             temperature.append(int(i[1]))
#     print(temperature)

import pandas
df=pandas.read_csv("weather_data.csv")
# print(df["temp"])

# print(df.to_dict())
# print(df["temp"].to_list())
# print(df["temp"].mean())
# print(df["temp"].max())
# to find a highest temp row data
#print(df.temp==df.temp.max())

#create a datafeame from scratch
df={
    "student":["Amy","Angela","Mnk"],
    "marks":[65,56,84]
}
data=pandas.DataFrame(df)
print(data)