# humidity vs time 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("SolarPrediction.csv")

# Combine the date from Data with the actual time from Time
df["DateTime"] = pd.to_datetime(
    df["Data"].astype(str).str.split().str[0]
    + " " + df["Time"],
    format="%m/%d/%Y %H:%M:%S"
)

# Sort observations by date and time
df = df.sort_values("DateTime")

# Split the data into four monthly periods
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


# Function to create a separate humidity graph
def plot_humidity(data, title):
    fig, ax = plt.subplots(figsize=(26, 7))

    ax.plot(
        data["DateTime"],
        data["Humidity"],
        color="darkcyan",
        linewidth=0.6,
        alpha=0.75
    )

    # Graph title and axis labels
    ax.set_title(title, fontsize=17, pad=16)
    ax.set_xlabel("Date", fontsize=14, labelpad=10)
    ax.set_ylabel("Humidity (%)", fontsize=14)

    # Humidity scale
    ax.set_ylim(0, 110)
    ax.set_yticks(range(0, 101, 10))

    # Show date labels every 2 days
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))

    # Style tick marks and labels
    ax.tick_params(axis="x", rotation=45, labelsize=10)
    ax.tick_params(axis="y", labelsize=11)

    # Grid lines
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.grid(axis="x", linestyle=":", alpha=0.15)

    # Display the date range for the selected month
    if not data.empty:
        ax.set_xlim(
            data["DateTime"].min(),
            data["DateTime"].max()
        )

    fig.tight_layout(pad=2.5)


# Create four independent graphs
plot_humidity(september, "Humidity Variation — September 2016")
plot_humidity(october, "Humidity Variation — October 2016")
plot_humidity(november, "Humidity Variation — November 2016")
plot_humidity(december, "Humidity Variation — December 2016")


plt.show()


