def test_plot_water_levels():
    from floodsystem.plot import plot_water_levels
    from floodsystem.stationdata import build_station_list
    plot_water_levels(build_station_list()[1],(2,5,6,3,6),(1,2,3,4,5))