import pandas as pd # import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.bz2") # read csv file and safe as dataframe

# print(df.head()) # print head of dataframe
# print(len(df)) # print length of dataframe
# print(df["City"]) # print column city from data file
# print(df["City"][1000]) # print value of 1000th element of column city from data file
# print(df["City"][1000:1010]) # print values of 1000th to 1010th element of column city from data file
# print(df[["Country","City"]]) # directly convert columns to a new dataframe, to get columns from interest

# df.drop(["AverageTemperatureUncertainty"], axis = 1, inplace = True) # drop column on actual dataframe

# print(df["AverageTemperature"].mean()) # get mean value of column AverageTemperature
# print(df["AverageTemperature"].min()) # get min value of column AverageTemperature
# print(df["AverageTemperature"].max()) # get max value of column AverageTemperature
# print(df["AverageTemperature"].sum()) # get sum value of column AverageTemperature
# print(df["AverageTemperature"].to_numpy()) # get numpy value of column AverageTemperature

# plt.hist(df["AverageTemperature"]) # create histrogram
# plt.show() # show histogram

print(df.loc[0]) # get first row of df
print(df.loc[0]["AverageTemperature"]) # get value in first row
print(dict(df.loc[0])) # convert first row to dictionary
print(df["City"].loc[0]) # first value from city
df_germany = df[df["Country"] == "Germany"] # get only germany
print(df_germany.head()) # check index
print(df_germany.iloc[0]) # start at index 0 with iloc
df_germany_france = df[(df["Country"] == "Germany") | (df["Country"] == "France")] # get germany or France
df_germany_france = df[(df["Country"] == "Germany") & (df["Country"] == "France")] # get germany and France