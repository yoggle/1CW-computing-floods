from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
stations_highest_rel_level = stations_highest_rel_level(stations, 10)
for station, relative_level in stations_highest_rel_level:
    print(f"{station.name}  {relative_level}")
