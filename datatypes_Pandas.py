import pandas as pd # import pandas as pd
import math

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

print(df.head())

df_city = df["City"].str.split(",", n=1, expand=True)
df["City"] = df_city[0]
df["Country"] = df_city[1]

print(df.head())