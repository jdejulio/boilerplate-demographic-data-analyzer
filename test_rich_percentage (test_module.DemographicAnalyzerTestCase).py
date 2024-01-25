import pandas as pd
import numpy as np
csv_file = "adult.data.csv"
df = pd.read_csv(csv_file)

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = len(df[df["hours-per-week"] == 1])

rich_percentage = round(len(df[(df["salary"] == ">50K") & (df["hours-per-week"] == 1)]) / num_min_workers * 100)
print(rich_percentage)