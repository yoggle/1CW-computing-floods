import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

stations=build_station_list()
update_water_levels(stations)

stations=stations_highest_rel_level(stations, 5)
for i in stations:
    dt = 2
    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(i, dates, levels, 3)


