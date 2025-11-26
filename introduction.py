import pandas as pd # import pandas as pd

# df = pd.read_csv("teilnehmer.csv") # read csv file and safe as dataframe
# print(df.head())
# print(df) # output dataframe

df = pd.read_csv("teilnehmer-semikolon.csv", sep = ";") # read file with semicolon delimeter, sep can be \t as well for tab
# use "" to escape seperators in csv file
print(df)
