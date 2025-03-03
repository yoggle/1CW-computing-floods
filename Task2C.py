from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
list_to_print = stations_highest_rel_level(stations, 10)
for station, relative_level in list_to_print:
    print(f"{station.name}  {relative_level}")
