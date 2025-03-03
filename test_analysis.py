import pytest
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit  

def test_polyfit():
    dates=[ datetime(2025, 2, i) for i in range (1,5)] # set the period from 2025.2.1-4
    levels = [i for i in range(1,5)]
    poly, d0 = polyfit(dates, levels, 2)
    time = mdates.date2num(dates)
    time1 = time - d0
    assert isinstance(poly, np.poly1d)
    assert d0 == time[0]
