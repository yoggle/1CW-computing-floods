# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    
    # 构建监测站列表
    stations = build_station_list()

    update_water_levels(stations)


    stations = stations_highest_rel_level(stations, 10)
    for i in stations:
        print(i.name, i.relative_water_level())




if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()