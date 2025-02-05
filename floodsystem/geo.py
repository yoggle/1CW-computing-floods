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
    theta = 2*np.asin(np.sqrt(havtheta))
    dist = 6371*theta
    return float(dist)

def stations_by_distance(stations,point):
    """ sort a list of stations by their distance from a point and return the sorted list of stations"""
    def dist(station,origin = point):
        return(haversine(origin,station.coord))

    return sorted(stations, key = dist)

def stations_within_radius(stations, centre, r):
    """ returns a list of stations within a set radius of a coordinate"""
    passed = []
    for i in stations:
        if haversine(origin = centre,new = i.coord) < r:
            passed.append(i)
    
    return passed

def rivers_with_stations(stations):
    """ returns a list with no duplicates of all rivers that have a station on them in a given list of stations"""
    rivers = []
    for i in stations:
        if i.river not in rivers:
            rivers.append(i.river)

    return rivers

def stations_by_rivers(stations):
    """ returns a dictionary of river names, and the stations on the river """
    dictionary = {}
    for i in rivers_with_stations(stations):
        templist = []
        for j in stations:
            if j.river == i:
                templist.append(j)
        dictionary[i] = templist
    
    return(dictionary)

def rivers_by_station_number(stations,N):
    """returns a list of the N rivers with the most monitoring stations, including stations with the same number of stations at the Nth one"""
    riverdict = stations_by_rivers(stations)
    big_list = []
    for i in riverdict.keys():
        big_list.append((i,len(riverdict[i])))
    big_list = sorted_by_key(big_list,1,reverse = True)
    stationnumber = big_list[N-1][1]
    small_list = []
    for i in big_list:
        if i[1] >= stationnumber:
            small_list.append(i)
    return small_list

