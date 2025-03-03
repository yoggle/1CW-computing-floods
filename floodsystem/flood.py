def stations_highest_rel_level(stations, N):
    '''Returns the first N stations with the highest relative water level'''
    stations = sorted(stations, key=lambda x: x.relative_water_level() or -float('inf'), reverse=True)

    toReturn = stations[:N]

    return(toReturn)
