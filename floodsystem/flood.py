from floodsystem.stationdata import build_station_list, update_water_levels


stations = build_station_list()
update_water_levels(stations)

def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    stations_over_threshold_none = []
    for station in stations:
        if station.typical_range is None:
            stations_over_threshold_none.append((station.name, relative_level))
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            stations_over_threshold.append((station.name, relative_level))
    return sorted(stations_over_threshold, key=lambda x:x[1], reverse=True)

def stations_highest_rel_level(stations, N):
    relative_water_level = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            relative_water_level.append((station, relative_level))
    return sorted(relative_water_level, key=lambda x:x[1], reverse=True)[:N]
