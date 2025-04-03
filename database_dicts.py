import csv
import pandas as pd

filename = "IHME_GBD_2010_MORTALITY_AGE_SPECIFIC_BY_COUNTRY_1970_2010.csv"

df = pd.read_csv(filename)



print(df["Country Code"].unique())
        

