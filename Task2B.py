# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_level_over_threshold


def run():
    
    # 构建监测站列表
    stations = build_station_list()

    # 更新所有站点的最新水位数据
    update_water_levels(stations)

    # 获取相对水位大于 0.8 的站点（按降序排序）
    threshold = 0.8
    stations_over_threshold = stations_level_over_threshold(stations, threshold)

    # 输出站点名称和相对水位
    for station, level in stations_over_threshold:
        print(f"{station.name} {level:.6f}")  # 保留 6 位小数




if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()