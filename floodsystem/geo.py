# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # 
import numpy as np
import math

def haversine(origin, new):
    """ compute the havrsine distance between two coordinate points given in tuples of (lattitude, longitude) in degrees"""
    phi1 = math.radians(origin[0])
    phi2 = math.radians(new[0])
    lambda1 = math.radians(origin[1])
    lambda2 = math.radians(new[1])
    havtheta = (np.sin((phi2-phi1)/2))**2 + np.cos(phi1)*np.cos(phi2)*(np.sin((lambda2-lambda1)/2))**2
    dist = 6371*havtheta
    return float(dist)

def stations_by_distance(stations,point):
    """ sort a list of stations by their distance from a point and return the sorted list of stations"""
    def dist(station,origin = point):
        return(haversine(origin,station.coord))

    return sorted(stations, key = dist)
