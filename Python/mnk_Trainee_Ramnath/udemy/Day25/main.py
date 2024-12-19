# with open('weather_data.csv',mode='r') as data:
#     list_name=data.readlines()
#     print(list_name)
#

# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures=[]
#     for row in data:
#         for i in row:
#             if i.isdigit():
#                temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data=pandas.read_csv('weather_data.csv')
# print(type(data))--> type-->Pandas.DataFrame
temp_list=data['temp'].to_list()
print(temp_list)
# avg_temp=sum(temp_list)/len(temp_list)
# print(avg_temp)

print(data['temp'].mean())

print(data['temp'].max())

# Todo: get Data in row
print(data[data.day=='Monday'])

# TODO: get max temp row
print(data[data.temp==data['temp'].max()])

# TODO: GET condition from day monday
monday = data[data.day=='Monday']
m_temp = monday['temp']
m_temp_f = m_temp* 9/5 + 32
print(m_temp_f)

# TODO : Create Dataframe from dictionary
dic={
    'students':['Ram',"surya","Hari"],
    "scores": [76,56,80]
}

data=pandas.DataFrame(dic)
print(data)
data.to_csv('students_data.csv')