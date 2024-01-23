### MUCHAS VARIABLES ESTÁN MAL, ES SOLO PARA PRUEBAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

csv_file = "adult.data.csv"
df = pd.read_csv(csv_file)

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = None
serie_race = df["race"].value_counts()
#print(serie_race)

#edad media hombres
men_df = df[df["sex"] == "Male"]
average_age_men = round(men_df["age"].mean(), 2)
#print(average_age_men)

# What is the percentage of people who have a Bachelor's degree?

bachelors_df = df[df["education"] == "Bachelors"]
percentage_bachelors = round((len(bachelors_df) / len(df)) *100, 2)
#print(percentage_bachelors)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
advanced_education_df = ((df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'))
percent_advanced_education_above50k = round((len(df[advanced_education_df]) / len(df)) * 100, 2)
#print(percent_advanced_education_above50k)
# What percentage of people without advanced education make more than 50K?
basic_education_df = ((~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'))
percent_basic_education_above50k = round((len(df[basic_education_df]) / len(df)) * 100, 2)
#print(percent_basic_education_above50k)
#print(basic_education_df)
# with and without `Bachelors`, `Masters`, or `Doctorate`



# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = round(len(df[df["hours-per-week"] == 1]) / len(df) * 100, 2)
#print(num_min_workers)

    # What country has the highest percentage of people that earn >50K?

max_salary = df["salary"].max()
#print(max_salary)
lines_max_salary = df[df["salary"] == max_salary]
#print(len(lines_max_salary))
highest_earning_country = lines_max_salary['native-country'].value_counts().idxmax()
#print(countries_max_salary)


highest_earning_country_percentage = round(len(df[(df["native-country"] == highest_earning_country) & (df["salary"] == max_salary)]) / len(df["native-country"] == highest_earning_country) * 100)
#print(highest_earning_country_percentage)
    # Identify the most popular occupation for those who earn >50K in India.

rich_indians = df[(df["native-country"] == "India") & (df["salary"] == max_salary)]
rich_indians_occupations = rich_indians["occupation"].value_counts().idxmax()
top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == max_salary)]
print(rich_indians_occupations)