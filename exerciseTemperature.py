import numpy as np
import pandas as pd

df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.bz2")

print(len(df[df["Country"] == "Spain"]))

df_germany = df[df["Country"] == "Germany"]

print(df_germany["AverageTemperature"].min())
print(df_germany["AverageTemperature"].max())

df_france = df[df["Country"] == "France"]

print("Deutschland: " + str(df_germany["AverageTemperature"].max()))
print("Frankreich: " + str(df_france["AverageTemperature"].max()))

print(len(df_germany[(df_germany["AverageTemperature"] <= -9) | 
                     (df_germany["AverageTemperature"] >= 22)]))

print(df.loc[df["Country"] == "China", "AverageTemperature"].min())