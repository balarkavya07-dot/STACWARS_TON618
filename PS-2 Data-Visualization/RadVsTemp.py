#**radiation vs temp**

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("SolarPrediction.csv")
print(df["Radiation"].head(20).to_list())
print("Minimum:", df["Radiation"].min())
print("Maximum:", df["Radiation"].max())

#It tells you the overall range of the radiation measurement
#It can help you notice unusually large or small values.
#It helps you understand the scale of the data.
grouping = df.groupby(pd.cut(df["Temperature"], bins=15), observed=True)["Radiation"]

#divides the temperature range into 15 intervals and summarizes radiation within each interval.
#groupby() collects rows into groups based on the intervals produced by pd.cut().
#Divide temperature into 15 ranges, group observations by those ranges, and collect their radiation value
avg, low, high = grouping.mean(), grouping.quantile(0.25), grouping.quantile(0.75)
x = [interval.mid for interval in avg.index] # find the midpoint of of each interval.
fig, ax = plt.subplots(figsize=(11, 6)) #representing figure and plotting area .

ax.plot(x, avg.values, marker="o", markersize=5, linewidth=2)
ax.fill_between(x, low.values, high.values, alpha=0.2) # alpha makes the shaded region transparent
ax.set_xlabel("Ambient Temperature (in Fahrenheit)", fontsize=12, labelpad=10)
ax.set_ylabel("Solar Radiation (W/m²)", fontsize=12, labelpad=10)
ax.set_title("Relationship Between Temperature and Solar Radiation", fontsize=14, pad=14)

ax.set_xticks(x)
ax.tick_params(axis="both", labelsize=10)
ax.grid(True, linestyle="--", alpha=0.35)

fig.tight_layout()
plt.show()

