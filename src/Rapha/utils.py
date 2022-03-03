# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:25:46 2022

@author: r.muema
"""

from datetime import datetime

def calculate_month(x):
    dt = datetime.strptime(x, "%d/%m/%Y %H:%M")
    return dt

def calculate_season(x):
    if (x  == 'Dec' or x == 'Jan' or x == 'Feb'):
        return 'Summer'
    elif (x == 'Mar' or x == 'Apr' or x == 'May'):
        return 'Autumn'
    elif (x == 'Jun' or x == 'Jul' or x == 'Aug'):
        return 'Winter'
    elif (x == 'Sep' or x == 'Oct' or x == 'Nov'):
        return 'Spring'