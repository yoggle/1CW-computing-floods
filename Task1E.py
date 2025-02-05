from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """print the names of, and the number of stations on the 9 rivers with the most monitoring stations"""
    print(rivers_by_station_number(build_station_list(),9))

if __name__ == "__main__":
    run()