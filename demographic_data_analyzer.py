import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    csv_file = "adult.data.csv"
    df = pd.read_csv(csv_file)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men_df = df[df["sex"] == "Male"]
    average_age_men = round(men_df["age"].mean(), 2)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_df = df[df["education"] == "Bachelors"]
    percentage_bachelors = round((len(bachelors_df) / len(df)) *100, 2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    higher_education = ((df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'))
    lower_education = ((~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'))

    # percentage with salary >50K
    higher_education_rich = round((len(df[higher_education]) / len(df)) * 100, 2)
    lower_education_rich = round((len(df[lower_education]) / len(df)) * 100, 2)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df["hours-per-week"] == 1])

    rich_percentage = round(len(df[df["hours-per-week"] == 1]) / len(df) * 100, 2)

    # What country has the highest percentage of people that earn >50K?
    ##se calcula el salario máximo: ">50K"
    max_salary = df["salary"].max()
    ##se extraen las filas con valor igual a max_salary
    lines_max_salary = df[df["salary"] == max_salary]
    highest_earning_country = lines_max_salary['native-country'].value_counts().idxmax()

    highest_earning_country_percentage = round(len(df[(df["native-country"] == highest_earning_country) & (df["salary"] == max_salary)]) / len(df["native-country"] == highest_earning_country) * 100)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[(df["native-country"] == "India") & (df["salary"] == max_salary)]
    top_IN_occupation = rich_indians["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
