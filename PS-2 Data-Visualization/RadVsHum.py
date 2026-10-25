#**--- radiation vs humidity**

import pandas as pd
#importing matplot library as plt
import matplotlib.pyplot as plt
#loading csv file and storing it into df 
df = pd.read_csv("SolarPrediction.csv")
#accessing Humidity and dividing it into 15 interval
df["HumidityGroup"] = pd.cut(df["Humidity"], bins=15)
#grouping 
humidity_groups = df.groupby("HumidityGroup", observed=True)["Radiation"]

humidity_avg = humidity_groups.mean()

humidity_low = humidity_groups.quantile(0.25)

humidity_high = humidity_groups.quantile(0.75)

humiditymidpoint = [interval.mid for interval in humidity_avg.index]
# plotting 
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(humiditymidpoint, humidity_avg.values,

       marker="o", markersize=4, linewidth=2,

       label="Average Radiation")

ax.fill_between(humiditymidpoint, humidity_low.values,

               humidity_high.values, alpha=0.2,

               label="Middle 50% of Readings")
# labelling the x and y axis and giving the title
ax.set_xlabel("Relative Humidity (%)", fontsize=12)
ax.set_ylabel("Solar Radiation (W/m²)", fontsize=12)
ax.set_title("Solar Radiation vs Humidity", fontsize=15)
ax.set_xticks(range(0, 101, 5))
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
ax.grid(True, which="major", linestyle="-", alpha=0.3)

ax.grid(True, which="minor", linestyle=":", alpha=0.2)

ax.legend()

fig.tight_layout()

plt.show()