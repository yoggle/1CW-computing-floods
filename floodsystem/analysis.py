import numpy as np
import matplotlib.dates as mdates

def polyfit(dates, levels, p):
    """Compute a least-squares polynomial fit of degree p to water level data."""
    date_nums = mdates.date2num(dates)
    
    d0 = date_nums[0]  # Reference point
    shifted_dates = date_nums - d0
    
    # Compute polynomial coefficients
    p_coeff = np.polyfit(shifted_dates, levels, p)
    
    # Create polynomial object
    poly = np.poly1d(p_coeff)
    
    return poly, d0
