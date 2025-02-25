import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def plot_water_levels(station, dates,levels):
    plt.plot(dates,levels, label = "Water Level")
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation = 45)
    plt.title(f"Station {station.name}")

    plt.plot(dates,[station.typical_range[1] for i in dates], color = "red", label = "Typical High")
    plt.plot(dates,[station.typical_range[0] for i in dates], color = "black", label = "Typical Low")
    plt.legend()
    plt.tight_layout()
    plt.show()
    return 0