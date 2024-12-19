import pandas

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrel_count=len(data[data['Primary Fur Color']=='Gray'])
cinnamon_squirrel_count=len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrel_count= len(data[data["Primary Fur Color"] == 'Black'])

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict={
    'Primary Fur Color':["Gray","Cinnamon","Black"],
    'count':[gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}
df=pandas.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_count.csv")