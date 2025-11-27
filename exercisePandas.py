import numpy as np
import pandas as pd

df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.bz2")

longitudeDir = df["Longitude"].str[-1]
df["Longitude"] = df["Longitude"].str[:-1].astype("float")
df.loc[longitudeDir == "W", "Longitude"] = df["Longitude"] * -1

latDir = df["Latitude"].str[-1]
df["Latitude"] = df["Latitude"].str[:-1].astype("float")
df.loc[latDir == "S", "Latitude"] = df["Latitude"] * -1

df["dt"] = pd.to_datetime(df["dt"])

print(df.loc[(df["Latitude"] > -10) & (df["Latitude"] < 10), "AverageTemperature"].mean())
print(df.loc[~((df["Latitude"] > -10) & (df["Latitude"] < 10)), "AverageTemperature"].mean())
print(df.loc[(df["Latitude"] < -10) | (df["Latitude"] > 10), "AverageTemperature"].mean())

df_country = df.groupby("Country").agg(avgT = ("AverageTemperature", np.mean))
df_country.sort_values("avgT", inplace = True, ascending = False)
print(df_country.iloc[0].name)

start_date =  pd.to_datetime("1990-01-01")
end_date = pd.to_datetime("2012-12-31")

df_filtered = df[(df["dt"] >= start_date) & (df["dt"] <= end_date)].copy()
df_filtered["dtYear"] = df_filtered["dt"].dt.year
res = df_filtered.groupby("dtYear").agg(avgT = ("AverageTemperature", np.mean))

res.sort_values("avgT", ascending = False, inplace = True)
print(res.iloc[0].name)