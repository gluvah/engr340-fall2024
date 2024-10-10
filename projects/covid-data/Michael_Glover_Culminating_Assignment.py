import sys
import numpy as np
import pandas as pd


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    first_case_rockingham = None
    first_case_harrisonburg = None

    for entry in data:
        date, county, state, cases, deaths = entry
        if county == 'Rockingham' and state == 'Virginia' and cases > 0:
            if first_case_rockingham is None:
                first_case_rockingham = date
        if county == 'Harrisonburg city' and state == 'Virginia' and cases > 0:
            if first_case_harrisonburg is None:
                first_case_harrisonburg = date
    print('The answers to the first question are:')
    print('The first positive COVID case in Rockingham County was on:', first_case_rockingham)
    print('The first positive COVID case in Harrisonburg was on:', first_case_harrisonburg)

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    rockingham_data = []
    harrisonburg_data = []

    #Filter the data to only include Rockingham and Harrisonburg County
    for entry in data:
        date, county, state, cases, deaths = entry
        if county == 'Harrisonburg city' and state == 'Virginia':
            harrisonburg_data.append(entry)
        elif county == 'Rockingham' and state == 'Virginia':
            rockingham_data.append(entry)

    #Track maximum new cases and the cooresponding date
    max_new_cases_harrisonburg = 0
    #In order to check for myself, I need to know the day in which this largest change occured
    max_new_cases_date_harrisonburg = None
    max_new_cases_rockingham = 0
    #In order to check for myself, I need to know the day in which this largest change occured
    max_new_cases_date_rockingham = None



    # Calculate daily new cases for Harrisonburg
    for i in range(1,len(harrisonburg_data)):
        previous_cases = harrisonburg_data[i-1][3]
        current_cases = harrisonburg_data[i][3]
        new_cases = current_cases - previous_cases
        if new_cases > max_new_cases_harrisonburg:
            max_new_cases_harrisonburg = new_cases
            max_new_cases_date_harrisonburg = harrisonburg_data[i][0]

    for i in range(1, len(rockingham_data)):
        previous_cases = rockingham_data[i - 1][3]
        current_cases = rockingham_data[i][3]
        new_cases = current_cases - previous_cases

        if new_cases > max_new_cases_rockingham:
            max_new_cases_rockingham = new_cases
            max_new_cases_date_rockingham = rockingham_data[i][0]

    print('\n')
    print('The answers to the second question are:')
    print('The greatest number of new daily cases recorded in Rockingham County were:', max_new_cases_rockingham, 'new cases, on', max_new_cases_date_rockingham)
    print('The greatest number of new daily cases recorded in Harrisonburg were:', max_new_cases_harrisonburg,
          'new cases, on', max_new_cases_date_harrisonburg)

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    #Put in empty lists to store the data for each county
    harrisonburg_data = []
    rockingham_data = []

    #Filter the data for each of the two counties
    for entry in data:
        date, county, state, cases, deaths = entry
        if county == 'Harrisonburg city' and state == 'Virginia':
            harrisonburg_data.append(entry)
        if county == 'Rockingham' and state == 'Virginia':
            rockingham_data.append(entry)

    #First, I calculate new daily cases for Harrisonburg
    #Put in empty lists to store the new daily data for Harrisonburg
    harrisonburg_new_daily_cases = []
    for i in range(1,len(harrisonburg_data)):
        previous_cases_h = harrisonburg_data[i-1][3]
        current_cases_h = harrisonburg_data[i][3]
        new_cases_h = current_cases_h - previous_cases_h
        harrisonburg_new_daily_cases.append((harrisonburg_data[i][0],new_cases_h))

    #Next, I calculate new daily cases for Rockingham
    #Put in empty lists to store the new daily data for Rockingham
    rockingham_new_daily_cases =[]
    for i in range(1,len(rockingham_data)):
        previous_cases_r = rockingham_data[i-1][3]
        current_cases_r = rockingham_data[i][3]
        new_cases_r = current_cases_r - previous_cases_r
        rockingham_new_daily_cases.append((rockingham_data[i][0],new_cases_r))

    #Finally, I can find the worst 7 day period. First, I will start with Harrisonburg.
    max_7_day_sum_h = 0
    max_7_day_period_h = None
    for i in range(len(harrisonburg_new_daily_cases)-6):
        running_7_day_sum = sum([harrisonburg_new_daily_cases[k][1] for k in range(i,i+7)])
        if running_7_day_sum > max_7_day_sum_h:
            max_7_day_sum_h = running_7_day_sum
            max_7_day_period_h = (harrisonburg_new_daily_cases[i][0], harrisonburg_new_daily_cases[i+6][0])

    #Moving on to Rockingham:
    max_7_day_sum_r = 0
    max_7_day_period_r = None
    for i in range(len(rockingham_new_daily_cases) - 6):
        running_7_day_sum = sum([rockingham_new_daily_cases[k][1] for k in range(i, i + 7)])
        if running_7_day_sum > max_7_day_sum_r:
            max_7_day_sum_r = running_7_day_sum
            max_7_day_period_r = (rockingham_new_daily_cases[i][0], rockingham_new_daily_cases[i + 6][0])

    #Display the answer!
    print('\n')
    print('The answers to the second question are:')
    print('The worst 7-day period for new COVID cases in Harrisonburg was from',
          max_7_day_period_h[0], 'to', max_7_day_period_h[1],
          'with a total of', max_7_day_sum_h, 'new cases.')
    print('The worst 7-day period for new COVID cases in Rockingham County was from',
          max_7_day_period_r[0], 'to', max_7_day_period_r[1],
          'with a total of', max_7_day_sum_r, 'new cases.')




    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

   # for (date, county, state, cases, deaths) in data:
   #     print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


