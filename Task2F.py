# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit




def run():
    
    stations = build_station_list()

    update_water_levels(stations)


    stations = stations_highest_rel_level(stations, 5)
    for i in stations:
        dt = 2
        dates, levels = fetch_measure_levels(
            i.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(i, dates, levels, 4)




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()