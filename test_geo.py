def test_haversine():
    from floodsystem.geo import haversine
    origin = (36,120)
    new = (4.872,47.1838)
    assert round(haversine(origin,new)) == 5890

def test_sort():
    from floodsystem.geo import stations_by_distance
    from floodsystem.stationdata import build_station_list
    stations_by_distance(build_station_list(),(37.2837,341.38447))