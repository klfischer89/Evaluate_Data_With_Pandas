import pandas as pd # import pandas as pd

df = pd.read_csv("./data/eine_Zeile.csv", sep = "|", lineterminator = "#") # read csv file and safe as dataframe with separator and lineterminator

print(df)
