# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """check if the typical range is a tuple, with highvalue greater than lowvalue, returns true if it is and false if it isn't"""
        if type(self.typical_range) == tuple and self.typical_range[1]-self.typical_range[0] > 0:
            return True
        else:
            return False

    def relative_water_level(self):
        """Return the relative water level as a fraction of the typical range"""
        if self.typical_range is None or self.latest_level is None:
            return None
        else:
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
    
def inconsistent_typical_range_stations(stations):
    inconsistent_stations=[]
    for station in stations:
        if station.typical_range_consistent()==False:
            inconsistent_stations.append(station)
    return inconsistent_stations

