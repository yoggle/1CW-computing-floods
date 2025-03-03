import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib.dates as mdates

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


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    time = mdates.date2num(dates)
    time = time - d0
    plt.plot(dates, levels, label='actual water level')
    plt.plot(dates, poly(time), label='fitted polynomial')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    upper=[station.typical_range[1] for i in range(len(dates))]
    lower=[station.typical_range[0] for i in range(len(dates))]
    plt.plot(dates, upper, label='typical high',linestyle='--')
    plt.plot(dates, lower, label='typical low',linestyle='--')
    plt.title('station: '+station.name)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
