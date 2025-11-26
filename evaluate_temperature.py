import pandas as pd # import pandas as pd

df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.bz2") # read csv file and safe as dataframe

# print(df.head()) # print head of dataframe
print(len(df)) # print length of dataframe
print(df["City"]) # print column city from data file
print(df["City"][1000]) # print value of 1000th element of column city from data file
print(df["City"][1000:1010]) # print values of 1000th to 1010th element of column city from data file
print(df[["Country","City"]]) # directly convert columns to a new dataframe, to get columns from interest

df.drop(["AverageTemperatureUncertainty"], axis = 1, inplace = True) # drop column on actual dataframe

print(df["AverageTemperature"].mean()) # get mean value of column AverageTemperature
print(df["AverageTemperature"].min()) # get min value of column AverageTemperature
print(df["AverageTemperature"].max()) # get max value of column AverageTemperature