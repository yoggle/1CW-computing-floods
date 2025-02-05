from floodsystem.geo import rivers_with_stations
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_rivers

def run():
    """ returns the first 10 rivers alphabetically that appear in the database and all the stations on the rivers aire, cam and thames """
    rivers = rivers_with_stations(build_station_list())
    print("There are ",len(rivers), " in the database, the first 10 in the alphabet are ", sorted(rivers)[:10])
    stations_on_each_river = stations_by_rivers(build_station_list())
    def alphabet_stations_of_river(stations):
        names = []
        for i in stations:
            names.append(i.name)
        return sorted(names)
    
    print("The stations on the rivers Aire, Cam and Thames are ",alphabet_stations_of_river(stations_on_each_river["River Aire"]), "\n",
    alphabet_stations_of_river(stations_on_each_river["River Cam"]), "\n", alphabet_stations_of_river(stations_on_each_river["River Thames"]),
    "\nrespectively.")

if __name__ == "__main__":
    run()

