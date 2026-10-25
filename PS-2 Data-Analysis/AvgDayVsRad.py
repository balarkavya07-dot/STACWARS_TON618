#**average day vs radiation**

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SolarPrediction.csv")

# Extract the hour from the actual observation time
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour

# Calculate average solar radiation for each hour
hourly_radiation = df.groupby("Hour")["Radiation"].mean()

# include the hours from 0 to 23 
allhours = range(24)
hourly_radiation = hourly_radiation.reindex(allhours, fill_value=0)

#  graph
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(hourly_radiation.index,hourly_radiation.values,marker="o",linewidth=1.8,markersize=6)

# Title and axis labels
ax.set_title("Average Solar Radiation by Time of Day", fontsize=14)
ax.set_xlabel("Hour of Day (24-hour)", fontsize=11)
ax.set_ylabel("Average Solar Radiation (W/m²)", fontsize=11)

# Show every hour on the X-axis
ax.set_xticks(range(24))

# Grid lines
ax.grid(True, linestyle="-", alpha=0.3)

# Adjust layout and display
fig.tight_layout()
plt.show()
