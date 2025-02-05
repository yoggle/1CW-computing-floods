from floodsystem.geo import stations_by_distance, haversine
from floodsystem.stationdata import build_station_list


def run():

    """ Take a list of stations and sort them by distance from a given coordinate with a function stored in geo"""
# sort stations that are imported by build_station_list
    sorted_stations = stations_by_distance(build_station_list(),(52.2053, 0.1218))
    toprint =[]
    for i in sorted_stations:
        toprint.append((i.name,i.river, haversine(origin = (52.2053, 0.1218),new = i.coord)))
    
    # print closest 10 then furthest 10 stations from the centre of cambridge
    print("The closest ten stations are: ",toprint[:10])
    print("The furthest 10 stations are: ",toprint[-10:])
    
    #return sorted list of stations
    return(sorted_stations)

if __name__ == "__main__":
    run()