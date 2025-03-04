from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import inconsistent_typical_range_stations


def stations_level_over_threshold(stations, tol):
    stations.remove(inconsistent_typical_range_stations(stations))
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
    inconsitent_stations = inconsistent_typical_range_stations(stations)
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and station not in inconsitent_stations:
            relative_water_level.append((station,relative_level))
    newlist = sorted(relative_water_level, key=lambda x:x[1], reverse=True)[:N]
    to_return = []
    for i in newlist:
        to_return.append(i[0])
    return to_return
