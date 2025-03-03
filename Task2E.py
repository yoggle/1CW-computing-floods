from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    dt = 10
    stationlist = build_station_list()
    update_water_levels(stationlist)
    stations = stations_highest_rel_level(stationlist,5)
    print(stations)
    count = 1
    for i in stations:
        dates, levels = fetch_measure_levels(i.measure_id,dt = datetime.timedelta(days = dt))
        plot_water_levels(i,dates,levels)
    
if __name__ == "__main__":
    run()