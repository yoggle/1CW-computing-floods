from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    s_id = 'test-s-id'
    m_id = 2
    label = 'some station'
    river = 'River X'
    town = 'My Town'
    # Range of water levels is the fifth argument when creating arbitary stations
    station1 = MonitoringStation(s_id, m_id, label, (0.2,2.5), (0.5,1.5), river, town) # Relative water level = 1 
    station2 = MonitoringStation(s_id, m_id, label, (0.1,1.8), (0.3,0.5), river, town) # Relative water level = 1
    station3 = MonitoringStation(s_id, m_id, label, (0.2,2.5), None, river, town) # Relative water level = None
    station4 = MonitoringStation(s_id, m_id, label, (0.5,3.0), (1.0,2.5), river, town) # Relative water level = 1
    # Set random current water levels for each station
    station1.latest_level = 1.5
    station2.latest_level = 0.5
    station3.latest_level = 2.0
    station4.latest_level = 2.5
    
    stations = [station1, station2, station3, station4]   
    assert stations_level_over_threshold(stations, 0.8) == [('some station', 1.0), ('some station', 1.0), ('some station', 1.0)]


def test_stations_highest_rel_level():
    s_id = 'test-s-id'
    m_id = 2
    label = 'some station'
    river = 'River X'
    town = 'My Town'
    # Range of water levels is the fifth argument when creating arbitary stationd
    station1 = MonitoringStation(s_id, m_id, label, (0.2,2.5), (0.5,1.5), river, town) # Relative water level = 2
    station2 = MonitoringStation(s_id, m_id, label, (0.1,1.8), (0.3,0.5), river, town) # Relative water level = 5.999999999999999
    station3 = MonitoringStation(s_id, m_id, label, (0.2,2.5), None, river, town) # Relative water level = None
    station4 = MonitoringStation(s_id, m_id, label, (0.5,3.0), (1.0,2.5), river, town) # Relative water level = 1
    # Set random current water levels for each station
    station1.latest_level = 2.5
    station2.latest_level = 1.5
    station3.latest_level = 1.0
    station4.latest_level = 2.5
    stations = [station1, station2, station3, station4]
    assert stations_highest_rel_level(stations, 2) == [station2,station1]
