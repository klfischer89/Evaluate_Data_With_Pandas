import pandas as pd # import pandas as pd
import math
import numpy as np

df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.bz2") # read csv file and safe as dataframe

x = float("nan")
# print(x)
# print(x == x)

# df = df[~pd.isna(df["AverageTemperature"])] # get only data that ist not NaN
# print(df)

df = df.dropna() # get only data that ist not NaN
# print(df)


df["City"] = df["City"] + ", " + df["Country"]
df.drop(["Country"], axis=1, inplace=True)

# print(df.head())

df_city = df["City"].str.split(",", n=1, expand=True)
df["City"] = df_city[0]
df["Country"] = df_city[1]

# print(df.head())

longitudeDir = df["Longitude"].str[-1]
df["Longitude"] = df["Longitude"].str[:-1].astype("float")
df.loc[longitudeDir == "W", "Longitude"] = df["Longitude"] * -1

latDir = df["Latitude"].str[-1]
df["Latitude"] = df["Latitude"].str[:-1].astype("float")
df.loc[latDir == "S", "Latitude"] = df["Latitude"] * -1

# print(df.head)

df["dt"] = pd.to_datetime(df["dt"])
df["dtYear"] = df["dt"].dt.year
# # print(df.head)
# print(df.loc[df["dt"].dt.year == 1849, "AverageTemperature"].mean())
# print(df.loc[df["dt"].dt.year == 2012, "AverageTemperature"].mean())

df.sort_values(by=["AverageTemperature"], inplace=True, ascending=False)

res = df.groupby(by=["dtYear"]).agg(
    avgTmp=("AverageTemperature", np.mean),
    minTmp=("AverageTemperature", np.min))

print(res.iloc[0])
print(res.loc[2000])
print(res.loc[1980:2014, "avgTmp"])

res.iloc[-1]
res.iloc[-1].name
res.sort_values("minTmp")
# print(res.head)