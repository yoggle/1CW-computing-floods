def test_plot_water_levels():
    from floodsystem.plot import plot_water_levels
    from floodsystem.stationdata import build_station_list
    plot_water_levels(build_station_list()[1],(2,5,6,3,6),(1,2,3,4,5))

def test_plot_water_level_with_fit():
    from floodsystem.plot import plot_water_level_with_fit
    from floodsystem.stationdata import build_station_list
    plot_water_level_with_fit(build_station_list()[4],(4,36,7,3,6),(5,7,3,86,6))