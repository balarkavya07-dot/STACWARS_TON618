#**radiation vs time**

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.dates as mdates
df = pd.read_csv("SolarPrediction.csv")
# Combine the date from 'Data' and actual observation time from 'Time'
df["DateTime"] = pd.to_datetime(
df["Data"].astype(str).str.split().str[0]
+ " " + df["Time"],
format="%m/%d/%Y %H:%M:%S"

)

# Sort observations chronologically
df = df.sort_values("DateTime")

#writing the observations ..
df = df[
(df["DateTime"] >= "2016-09-01")
& (df["DateTime"] < "2017-01-01")
]
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
df["DateTime"],
df["Radiation"],
color="blue",
linewidth=0.6,
alpha=0.8
)

# Title and axis labels
ax.set_title("Solar Radiation Over Time (Sep–Dec 2016)",

            fontsize=17, pad=15)
ax.set_xlabel("Date", fontsize=14, labelpad=10)
ax.set_ylabel("Radiation (W/m²)", fontsize=14, labelpad=10)

ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %Y"))
# Rotate date labels
ax.tick_params(axis="x", labelsize=10, rotation=35)
ax.tick_params(axis="y", labelsize=11)
# Grid lines
ax.grid(True, which="major", linestyle="-", alpha=0.25)
# Keep the date range within September–December
ax.set_xlim(
pd.Timestamp("2016-09-01"),
pd.Timestamp("2017-01-01")
)
fig.tight_layout()
plt.show()