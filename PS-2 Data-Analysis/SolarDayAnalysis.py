# Part C - Solar Day Analysis

import pandas as pd

#read the file
df = pd.read_csv("SolarPrediction.csv")
print(df.head(2))

#Step 1: make one proper datetime column
#in data part we do not need 12:00:00 so cut it out and join time part instead
#split(" ") cuts the text at every spacebar, [0] takes the first piece i.e. date only
only_date = df["Data"].str.split(" ").str[0]

#join the date and the Time column into one text
full_text = only_date + " " + df["Time"]

#convert the text into a real datetime using .to_datetime() function
df["Datetime"] = pd.to_datetime(full_text)
#do the same for sunrise and sunset too
df["SunRise"] = pd.to_datetime(only_date + " " + df["TimeSunRise"])
df["SunSet"] = pd.to_datetime(only_date + " " + df["TimeSunSet"])
print(df.head(2))

#a column that has only the date (needed for grouping in daily average and daily max radiation)
df["Date"] = df["Datetime"].dt.date

#Step 2: daily maximum and daily average radiation
daily_max = df.groupby("Date")["Radiation"].max()
daily_avg = df.groupby("Date")["Radiation"].mean()
print(daily_max)
#put both in one table
report = pd.DataFrame()
report["DailyMax"] = daily_max
report["DailyAvg"] = daily_avg
print(report.head(2))

#Step 3: date with the highest radiation
#make a list of all radiation use max to find max and find its row number
list_radiation = df["Radiation"].tolist()
max_radiation = max(list_radiation)
row_number = list_radiation.index(max_radiation)
#the whole row at that number
peak = df.loc[row_number]   
#date with maximum radiation and the corresponding radiation
print(f"****************************\n*       peak deails        *\n****************************")
print("Highest radiation:", peak["Radiation"])
print("Date:", peak["Date"])

#Step 4: time, temperature, humidity and wind speed at the max radiation
print("Time:", peak["Datetime"].time())
print("Temperature:", peak["Temperature"])
print("Humidity:", peak["Humidity"])
print("Wind speed:", peak["Speed"])

#Step 5: how long after sunrise did the peak happen?
#subtracting two datetimes gives a time difference
difference = peak["Datetime"] - peak["SunRise"]
print("Sunrise:", peak["SunRise"].time())
print("Sunset:", peak["SunSet"].time())
print("Time after sunrise:", difference)

#Step 6: top 5 days with the highest average radiation
#sort and take dates with largest values 
top5 = daily_avg.sort_values().tail(5)
#in this these 5 have largest values but they themselves are from smallest to largest
#reverse them so they are in decresing order like their postion
reversed_top5=top5[::-1]
print(f"*************************************************\n*      Top 5 days by average radiation:         *\n*************************************************")
print(reversed_top5)


#making separate text file of daily_avg and daily_max
with open("daily_report.txt","w") as f:
    f.write("Date           daily_avg     daily_max \n")
    for date in daily_max.index:
        line=f"{date}       {str(round(daily_avg[date],2))}       {str(round(daily_max[date],2))}\n"
        f.write(line)





