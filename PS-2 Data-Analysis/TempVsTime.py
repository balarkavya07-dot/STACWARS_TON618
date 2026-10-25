#temp vs time 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("SolarPrediction.csv")

# Combining the data
df["DateTime"] = pd.to_datetime(
    df["Data"].astype(str).str.split().str[0]
    + " " + df["Time"],
    format="%m/%d/%Y %H:%M:%S"
)

# Sort observations by date and time
df = df.sort_values("DateTime")

# Split the data into four monthly periods...
september = df[
    (df["DateTime"] >= "2016-09-01") &
    (df["DateTime"] < "2016-10-01")
]

october = df[
    (df["DateTime"] >= "2016-10-01") &
    (df["DateTime"] < "2016-11-01")
]

november = df[
    (df["DateTime"] >= "2016-11-01") &
    (df["DateTime"] < "2016-12-01")
]

december = df[
    (df["DateTime"] >= "2016-12-01") &
    (df["DateTime"] < "2017-01-01")
]


# Function to create a separate temperature graph
def plot_temperature(data, title):

    fig, ax = plt.subplots(figsize=(26, 7))

    ax.plot(
        data["DateTime"],
        data["Temperature"],
        color="darkorange",
        linewidth=0.6,
        alpha=0.75
    )

    # Graph title and axis labels
    ax.set_title(title, fontsize=17, pad=16)
    ax.set_xlabel("Date", fontsize=14, labelpad=10)
    ax.set_ylabel("Temperature", fontsize=14, labelpad=12)

    # Detailed temperature scale based on the data
    if not data.empty:
        min_temp = data["Temperature"].min()
        max_temp = data["Temperature"].max()

        lower = int(5 * (min_temp // 5))
        upper = int(5 * (max_temp // 5 + 1))

        ax.set_ylim(lower, upper)
        ax.set_yticks(range(lower, upper + 1, 5))
        ax.set_yticks(range(lower, upper + 1, 1), minor=True)

    # Date labels every day
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))

    # Minor tick marks every 6 hours
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=6))

    # Style the tick marks and labels
    ax.tick_params(axis="x", which="major", rotation=45, labelsize=10)
    ax.tick_params(axis="x", which="minor", length=3, color="gray")
    ax.tick_params(axis="y", which="major", labelsize=10, length=5)
    ax.tick_params(axis="y", which="minor", length=2, color="gray")

    # Major and minor gridlines
    ax.grid(axis="y", which="major", linestyle="--", alpha=0.35)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.12)
    ax.grid(axis="x", which="major", linestyle=":", alpha=0.25)

    # Display the complete date range
    if not data.empty:
        ax.set_xlim(data["DateTime"].min(), data["DateTime"].max())

    # Adjust spacing so labels are not clipped
    fig.tight_layout(pad=2.5)


# Create four independent graphs
plot_temperature(september, "Temperature Variation — September 2016")
plot_temperature(october, "Temperature Variation — October 2016")
plot_temperature(november, "Temperature Variation — November 2016")
plot_temperature(december, "Temperature Variation — December 2016")

# Display all graphs
plt.show()