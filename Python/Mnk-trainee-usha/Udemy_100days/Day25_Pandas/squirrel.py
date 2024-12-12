import pandas
df=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels=len(df[df["Primary Fur Color"]=="Gray"])
Cinnamon_squirrels=len(df[df["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(df[df["Primary Fur Color"]=="black"])
print(f"grey_color_squirrels: {grey_squirrels}")
print(f"Cinnamon_color_squirrels: {Cinnamon_squirrels}")
print(f"black_color_squirrels: {black_squirrels}")

#creating a dataframe
data_dict={
    "Fur Color":["Grey","Cinnamon","black"],
    "Count":[grey_squirrels,Cinnamon_squirrels,black_squirrels]
}
data=pandas.DataFrame(data_dict)
data.to_csv("squireel_count.csv")