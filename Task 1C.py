import floodsystem.geo as lib
from floodsystem.stationdata import build_station_list

def run():
    
    stations = lib.stations_within_radius(build_station_list(),(52.2053, 0.1218),10)
    stations_to_print = []
    for i in stations:
        stations_to_print.append(i.name)
    print(sorted(stations_to_print))

if __name__ == "__main__":
    run()