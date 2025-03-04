from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_town
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
from floodsystem.utils import sorted_by_key

#create list of all stations
all_of_em = build_station_list()

#add wet info

update_water_levels(all_of_em)

#create dictionary of stations by town
town_dict = stations_by_town(all_of_em)

#remove stations without water level information

for i in town_dict.keys():
    for j in town_dict[i]:
        if j.relative_water_level() == None:
            town_dict[i].remove(j)

#remove towns from dict with no stations with wet data

town_dict = {k: v for k,v in town_dict.items() if v}



#function that takes in list of stations associated with a town and outputs a risk factor for the town
def how_scary(town):
    fear_factor = 0
    #parse the list of stations inputted and sum their risk factor
    for i in town:
        if i.relative_water_level() == None:
            pass
        elif i.relative_water_level() < 1:
            fear_factor += 0
        else:
            grads = []
            for j in range(3):
                dates, levels = fetch_measure_levels(i.measure_id,dt = datetime.timedelta(days = (j+2)))
                try:
                    poly, d0 = polyfit(dates,levels,1)
                except:
                    grads = [0,0,0]
                    break
                grads.append(poly(1)-poly(0))
            #the folowing fear factor assumes that only new flood risks are important, 
            #so disproportionately gives risk factor to recent upwards fluctuations in river level
            fear_factor += i.relative_water_level()*(10*grads[0]+5*grads[1] + grads[2])

    #return value for risk factor, sum of risks due to stations / number of stations near town
    return fear_factor/len(town)


#create a list of tuples with town name and risk factor
town_risks = []
for i in town_dict.keys():
    town,risk = i, how_scary(town_dict[i])
    town_risks.append((town,risk))

town_risks = sorted_by_key(town_risks,1,reverse=True)

#print the towns with non-zero risk factor, with high risk for large increasing recent water level, medium risk for slowly increasing water level
#and low risk for those with decreasing water level
for i in town_risks:
    if i[1] > 0.01:
        print(f"The risk in {i[0]} is High")
    elif i[1] > 0:
        print(f"The risk in {i[0]} is Medium")
    elif i[1] == 0:
        pass
    else:
        print(f"The risk in {i[0]} is Low")