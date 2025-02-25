from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime

stationlist = build_station_list()

dt = 50

dates, levels = fetch_measure_levels(stationlist[5].measure_id
                           
                        , dt = datetime.timedelta(days = dt))

plot_water_levels(stationlist[5],dates,levels)