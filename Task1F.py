from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """prints all stations with inconsistent typical ranges"""
    toprint = []
    for i in inconsistent_typical_range_stations(build_station_list()):
        toprint.append(i.name)
    print(sorted(toprint))

if __name__ == "__main__":
    run()