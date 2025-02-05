def test_haversine():
    from floodsystem.geo import haversine
    origin = (36,120)
    new = (4.872,47.1838)
    assert round(haversine(origin,new)) == 5890

def test_sort():
    from floodsystem.geo import stations_by_distance
    from floodsystem.stationdata import build_station_list
    stations_by_distance(build_station_list(),(37.2837,341.38447))

def test_stations_in_area():
    from floodsystem.geo import stations_within_radius
    from floodsystem.stationdata import build_station_list
    assert type(stations_within_radius(build_station_list,(52.2053, 0.1218),100)) == list

def test_rivers_with_stations():
    from floodsystem.geo import rivers_with_stations
    from floodsystem.stationdata import build_station_list
    assert rivers_with_stations(build_station_list) == list

def test_stations_by_rivers():
    from floodsystem.geo import stations_by_rivers, rivers_with_stations
    from floodsystem.stationdata import build_station_list
    assert stations_by_rivers(build_station_list)["River Cam"] == list

def test_lots_of_stations():
    from floodsystem.geo import rivers_by_station_number
    from floodsystem.stationdata import build_station_list
    assert len(rivers_by_station_number(build_station_list,6)) >= 6