def second_question(data):
    """
    Write code to address the following question: Use print() to display your responses.
    What day was the greatest number of new daily cases recorded in Harrisonburg?
    What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Initialize lists to store data for each county
    harrisonburg_data = []
    rockingham_data = []

    # Filter the data for Harrisonburg and Rockingham County
    for entry in data:
        date, county, state, cases, deaths = entry
        if county == 'Harrisonburg' and state == 'Virginia':
            harrisonburg_data.append(entry)
        elif county == 'Rockingham' and state == 'Virginia':
            rockingham_data.append(entry)

    # Track maximum new cases and corresponding dates
    max_new_cases_harrisonburg = 0
    max_new_cases_date_harrisonburg = None
    max_new_cases_rockingham = 0
    max_new_cases_date_rockingham = None

    # Calculate daily new cases for Harrisonburg
    for i in range(1, len(harrisonburg_data)):
        previous_cases = harrisonburg_data[i - 1][3]
        current_cases = harrisonburg_data[i][3]
        new_cases = current_cases - previous_cases

        if new_cases > max_new_cases_harrisonburg:
            max_new_cases_harrisonburg = new_cases
            max_new_cases_date_harrisonburg = harrisonburg_data[i][0]

    # Calculate daily new cases for Rockingham
    for i in range(1, len(rockingham_data)):
        previous_cases = rockingham_data[i - 1][3]
        current_cases = rockingham_data[i][3]
        new_cases = current_cases - previous_cases

        if new_cases > max_new_cases_rockingham:
            max_new_cases_rockingham = new_cases
            max_new_cases_date_rockingham = rockingham_data[i][0]

    # Print the results
    print('The day with the greatest number of new daily cases in Harrisonburg was on:', max_new_cases_date_harrisonburg,
          'with', max_new_cases_harrisonburg, 'new cases.')
    print('The day with the greatest number of new daily cases in Rockingham County was on:', max_new_cases_date_rockingham,
          'with', max_new_cases_rockingham, 'new cases.')

    return