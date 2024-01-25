import pandas as pd
import numpy as np


csv_file = "adult.data.csv"
df = pd.read_csv(csv_file)
'''# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
higher_degrees = (df["education"] == "Bachelors") | (df['education'] == "Masters") & (df["education"] == "Doctorate")
higher_salary = df['salary'] == '>50K'
lower_degrees = ~(df["education"] == "Bachelors") | (df['education'] == "Masters") | (df["education"] == "Doctorate")
higher_education = df[higher_degrees & higher_salary]
lower_education = df[lower_degrees & higher_salary]
#print(higher_education)

#print(lower_education)
    # percentage with salary >50K
#
higher_education_rich = len(higher_education) / len(higher_salary) * 100
lower_education_rich = round((len(lower_education) / len(lower_degrees)) * 100, 2)
print(higher_education_rich)
print(lower_education_rich)'''



high_ed_high_sal = df[(df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")]
high_ed_percentage_rich = len(high_ed_high_sal) / len(df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]) * 100
low_ed_high_sal = df[(df["education"].isin(['HS-grad', '11th', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th'])) & (df["salary"] == ">50K")]
low_ed_percentage_rich = len(low_ed_high_sal) / len(df[df["education"].isin(['HS-grad', '11th', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th'])]) * 100

print(low_ed_percentage_rich)