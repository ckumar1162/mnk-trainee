import datetime as dt
import pandas as pd

today = dt.datetime.now()
today_date = (today.month,today.day)

data = pd.read_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\Birthday+Wisher+(Day+32)+start\birthday-wisher-normal-start\birthdays.csv")
