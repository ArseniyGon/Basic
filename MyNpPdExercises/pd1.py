import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prd = pd.Period(freq = 'S', year = 2000, month = 2,
                day = 21, hour = 8, minute = 21)
print(prd)
print(prd.year)

prd = pd.Period(freq = 'T', year = 2006, month = 10,
                hour = 15, minute = 49)

print(prd)
print(prd.year)

prd = pd.Period(freq = 'D', year = 2001, month = 1, day = 21)
print(prd)
print(prd.day)

prd = pd.Period(freq = 'Q', year = 2006, quarter = 1)
print(prd)
print(prd.day)

df = pd.read_csv("apple.csv", parse_dates = ["date"], index_col ="date")

print(df[:10])

monthly_resampled_data = df.close.resample('M').mean()
print(monthly_resampled_data)

df = pd.read_csv("apple.csv", parse_dates=["date"], index_col ="date")
weekly_resampled_data = df.open.resample('W').mean()
print(weekly_resampled_data)

df = pd.read_csv("apple.csv", parse_dates=["date"], index_col ="date")
Quarterly_resampled_data = df.open.resample('Q').mean()
print(Quarterly_resampled_data)








