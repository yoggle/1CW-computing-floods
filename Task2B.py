from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_level_over_threshold


def run():
    
    
    stations = build_station_list()
    update_water_levels(stations)

    threshold = 0.8
    stations_over_threshold = stations_level_over_threshold(stations, threshold)

    for station, level in stations_over_threshold:
        print(f"{station.name} {level:.6f}") 




if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
