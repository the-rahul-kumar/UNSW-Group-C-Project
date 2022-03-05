# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:49:50 2022

@author: r.muema
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import utils

# Load NSW data
forecastdemand_nsw = pd.read_csv("Datasets/forecastdemand_nsw.csv")
temperature_nsw = pd.read_csv("Datasets/temperature_nsw.csv")
totaldemand_nsw = pd.read_csv("Datasets/totaldemand_nsw.csv")

# # Load QLD data
# forecastdemand_qld = pd.read_csv("Datasets/forecastdemand_qld.csv")
# temprature_qld = pd.read_csv("Datasets/temprature_qld.csv")
# totaldemand_qld = pd.read_csv("Datasets/totaldemand_qld.csv")

# # Load SA data
# forecastdemand_sa = pd.read_csv("Datasets/forecastdemand_sa.csv")
# temprature_sa = pd.read_csv("Datasets/temprature_sa.csv")
# totaldemand_sa = pd.read_csv("Datasets/totaldemand_sa.csv")

# # Load VIC data
# forecastdemand_vic = pd.read_csv("Datasets/forecastdemand_vic.csv")
# temprature_vic = pd.read_csv("Datasets/temprature_vic.csv")
# totaldemand_vic = pd.read_csv("Datasets/totaldemand_vic.csv")

# Combine temperature and demand 
combined_temperature_totaldemand_nsw = pd.merge(temperature_nsw, totaldemand_nsw, on="DATETIME")

# Create extra fields from the data
combined_temperature_totaldemand_nsw['DATETIME'] = combined_temperature_totaldemand_nsw['DATETIME'].apply(lambda x: utils.calculate_month(x))
combined_temperature_totaldemand_nsw['YEAR'] = combined_temperature_totaldemand_nsw['DATETIME'].dt.year
combined_temperature_totaldemand_nsw['MONTH'] = combined_temperature_totaldemand_nsw['DATETIME'].dt.month_name().str[:3]
combined_temperature_totaldemand_nsw['SEASON'] = combined_temperature_totaldemand_nsw['MONTH'].apply(lambda x: utils.calculate_season(x))

# Save combined dataframe
combined_temperature_totaldemand_nsw.to_csv('Datasets/combined_temperature_totaldemand_nsw.csv',header=combined_temperature_totaldemand_nsw.columns, index=False)
