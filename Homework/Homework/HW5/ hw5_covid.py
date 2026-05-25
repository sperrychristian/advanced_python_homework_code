"""
Starter code: Fetch covid cases data for Utah from the CDC API

Dataset:
Weekly United States COVID-19 Cases by State (ARCHIVED)

IMPORTANT:
- This dataset is WEEKLY, not daily.  The day shown is the end of week date.
- This starter code prints RAW JSON text.
- You are expected to parse and analyze the data.
"""

# librarys we'll use in the code 
import requests
import csv
import json


# accessing the csv file
with open('/workspaces/advanced_python_homework_code/Homework/Homework/HW5/states.csv', newline='') as file:
    reader = csv.reader(file)

    # dictionary to store state information that will be used in final analysis
    high_state_information = {}

    # setting up a for loop to iterate through each state 
    for row in reader:

        DATASET_ID = "pwn4-m3yp"
        BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

        # assigning a new state and population each time the loop iterates 
        state = row[0].strip()
        population = row[1].strip()

        params = { 
    "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
        
        req = requests.get(BASE_URL, params=params)
        # convert to json
        data = req.json()

        # establishing a nested for loop to iterate through each states information and print the average new cases and date with the highest number of new cases 
        counter = 0
        weekly_cases = 0
        highest_new_cases = 0
        highest_new_cases_date = ''
        highest_new_number_percentage = ''

        # dictionary mapping month names to their numeric counterpart
        month_names = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'}

        # dictionary that will be used to hold monthly totals
        monthly_totals = {}

        
        print(f'State Name: {state}')
        print('\n')

        for period in data:
            counter += 1

            # update weekly cases 
            weekly_cases += float(period['new_cases'])

            # update new highest number of cases and date if needed 
            if float(period['new_cases']) > highest_new_cases:
                highest_new_cases = float(period['new_cases'])
                highest_new_cases_date = period['end_date'][0:10] # trimming this line so it only grabs the date portion of the string

            # grab the year and month from the end_date string and add this weeks cases to that months running total
            month_key = period['end_date'][0:7]
            # # establishing in the monthly totals dictionary if it doesn't exist yet
            if month_key not in monthly_totals:
                monthly_totals[month_key] = 0 
            monthly_totals[month_key] += float(period['new_cases'])

        # calculating average new weekly cases 
        avg_new_cases = round(weekly_cases/counter, 2) # rounding to match the example formatting

        # find the month with the highest total new cases and calculate what % of the population it represents

        # calculate the highest month in the monthly totals dictionary, key= points at the value of each key to calculate the max off of
        highest_month_key = max(monthly_totals, key=monthly_totals.get)
            # setting the highest month total = to a variable to reference in the print statement
        highest_month_total = monthly_totals[highest_month_key]
        highest_month_percentage = round((highest_month_total/int(population)) * 100, 2)

            # isolating year and month in the highest month key to convert to a string for the correct print output
        year = highest_month_key[0:4]
        month_numeric = highest_month_key[5:7]
        month_print = month_names[month_numeric]

        # creating a new JSON file for each state and translating the information to it
        with open(f'/workspaces/advanced_python_homework_code/Homework/Homework/HW5/state_json/{state}.json', 'w') as file:
            json.dump(data, file, indent=2)

        print(f'Average number of new weekly cases for the entire state dataset: {avg_new_cases}')
        print(f'Date with the highest new number of covid cases: {highest_new_cases_date} ({highest_new_cases})')
        print(f'Month and Year, with the highest new number of covid cases: {month_print} {year} ({highest_month_total})')
        print(f'Month and Year, with highest new number, percentage of population: {highest_month_percentage}% (Population: {population})')
        print('\n-------------------------------------------\n')

        # add to the high state info dictionary 
        high_state_information[state] = {'highest_month_percentage': float(highest_month_percentage), 'output_string': f'{state} - {highest_month_percentage}% in {month_print} {year} ({highest_month_total} cases: Population {population})'}

# summary that prints at the end 
maximum_percentage_all_states = 0
state_with_max = ''

minimum_percentage_all_states = 100000000000000
state_with_min = ''

# loop through all state codes in my dictionary and set a new maximimum
for state_code in high_state_information:
    summary = high_state_information[state_code]
    current_percentage = summary['highest_month_percentage']
    if current_percentage > maximum_percentage_all_states:
        maximum_percentage_all_states = current_percentage
        state_with_max = state_code

# loop through all state coes in my dictionary and set a new minimum
for state_code in high_state_information:
    summary = high_state_information[state_code]
    current_percentage = summary['highest_month_percentage']
    if current_percentage < minimum_percentage_all_states:
        minimum_percentage_all_states = current_percentage
        state_with_min = state_code

print('==================== SUMMARY ACROSS ALL STATES ====================\n')
print('State with HIGHEST percentage of population during its highest month:')
print(high_state_information[state_with_max]['output_string'])
print()

print('State with LOWEST percentage of population during its highest month:')
print(high_state_information[state_with_min]['output_string'])




'''
Your program should compute the following statistics and print the output for each state:


State name: <STATE>

Average number of new weekly cases for the entire state dataset:
Date with the highest new number of covid cases:
Month and Year, with the highest new number of covid cases:
Month and Year, with highest new number, percentage of population:
'''

'''
States with Highest and Lowest Percentages
In addition to statistics for each state, calculate the states with State with HIGHEST percentage of population during its highest month of new covid cases:

Sample output below

Note:  I removed all states but UT and VT in the sample output below.  Your program will find the real states with highest and lowest percentages.

 

State name: UT

Average number of new weekly cases for the entire state dataset: 6343.79
Date with the highest new number of covid cases: 2022-01-19 (76633)
Month and Year, with the highest new number of covid cases: January 2022 (228454)
Month and Year, with highest new number, percentage of population: 6.98% (Population: 3271616)

------------------------------------------------------------

State name: VT

Average number of new weekly cases for the entire state dataset: 891.58
Date with the highest new number of covid cases: 2022-01-12 (12286)
Month and Year, with the highest new number of covid cases: January 2022 (37504)
Month and Year, with highest new number, percentage of population: 5.83% (Population: 643077)

------------------------------------------------------------

==================== SUMMARY ACROSS ALL STATES ====================

State with HIGHEST percentage of population during its highest month:
UT - 6.98% in January 2022 (228454 cases; Population: 3271616)

State with LOWEST percentage of population during its highest month:
VT - 5.83% in January 2022 (37504 cases; Population: 643077)

 

Other Programming/Data Requirements
Use the CDC API listed above to retrieve JSON data
- Convert the JSON response into Python data structures
- Save each state’s raw JSON data as <STATE>.json
- Output results to the console
'''