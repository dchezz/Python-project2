#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:55:04 2020

@author: dario
"""
import csv
list_everything=[]
with open("synergy_logistics_database.csv", "r", encoding='utf-8-sig') as full_database_csv:
    lecture = csv.DictReader(full_database_csv)    
    for line in lecture:
        list_everything.append(line)
    

#Function that lits all the routes by frequancy and total incomes, either for exportations or importations.
#Parameters: "Exports" and "Imports"
def f1(direction):
    route_freq = 0
    counter_income = 0
    counter_routes = []
    list_routes = []
    ordered_routes = []
    sum_total = 0
    for register in list_everything:
        if register["direction"] == direction:
            current_route = [register["origin"], register["destination"]]
            sum_total += int(register["total_value"]) 
            if current_route not in counter_routes:
                for route_register in list_everything:
                    if current_route == [route_register["origin"], route_register["destination"]] and route_register["direction"] == direction:
                        counter_income += int(route_register["total_value"])
                        route_freq +=1
                counter_routes.append(current_route)
                list_routes.append([register["origin"], register["destination"], counter_income])
                ordered_routes.append([register["origin"], register["destination"], route_freq])
                counter_income = 0
                route_freq = 0
        list_routes.sort(reverse = True, key = lambda x:x[2])
        ordered_routes.sort(reverse = True, key = lambda y:y[2])
    return list_routes, sum_total, ordered_routes
            
export_list = f1("Exports")[0]
import_list = f1("Imports")[0]
export_incomes = f1("Exports")[1]
import_incomes = f1("Imports")[1]
ordered_exports = f1("Exports")[2]
ordered_imports = f1("Imports")[2]

#Exportation list that represent the 80 percent of total incomes 
sum_per = 0
per_list = []   
for percentage in export_list:
    per_income = percentage[2]*100/export_incomes
    sum_per += per_income
    per_list.append(per_income)
    if sum_per >= 80:
        break
#print("****The exportation list ordered by income revelance is: \n")
#print(per_list)

#Importation list that represent the 80 percent of total incomes 
sum_per2 = 0
per_list2 = []   
for percentage2 in import_list:
    per_income2 = percentage2[2]*100/import_incomes
    sum_per2 += per_income2
    per_list2.append(per_income2)
    if sum_per2 >= 80:
        break
#print("\n ****The importation list ordered by income revelance is: \n")
#print(per_list2)

#Exportation list that represent the 60 percent of total movements 
sum_per3 = 0
per_list3 = []   
for percentage3 in ordered_exports:
    per_income3 = percentage3[2]*100/15408
    sum_per3 += per_income3
    per_list3.append(per_income3)
    if sum_per3 >= 60:
        break
#print("****The exportation list ordered by movement revelance is: \n")
#print(per_list3)

#Importation list that represent the 60 percent of total movements
sum_per4 = 0
per_list4 = []   
for percentage4 in ordered_imports:
    per_income4 = percentage4[2]*100/3648
    sum_per4 += per_income4
    per_list4.append(per_income4)
    if sum_per4 >= 60:
        break
#print("\n ****The importation list ordered by movement revelance is: \n")
#print(per_list4)

#Plots relating % of incomes and %of movements
from matplotlib import pyplot as plt
plt.plot(per_list3[0:10], per_list[0:10], label = "Exports")
plt.xlabel("% of movements")

from matplotlib import pyplot as plt
plt.plot(per_list4[0:10], per_list2[0:10], label = "Imports")
plt.ylabel("% of incomes")
plt.legend()
