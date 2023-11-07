import time
import pandas as pd
import numpy as np

CITY_BIKEDATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city_input():
    while True:
        city = input("Please enter the city you want to analyze (Chicago, New York City, or Washington): ").strip().lower()
        if city in CITY_BIKEDATA:
            return city
        else:
            print("Invalid input. Please enter a valid city.")

def get_month_input():
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Please enter the month you want to filter by (January, February, March, April, May, June, or 'all' for all months): ").strip().lower()
        if month in valid_months:
            return month
        else:
            print("Invalid input. Please enter a valid month or 'all'.")

def get_day_input():
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Please enter the day of the week you want to filter by (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or 'all' for all days): ").strip().lower()
        if day in valid_days:
            return day
        else:
            print("Invalid input. Please enter a valid day or 'all'.")

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city_input()
    month = get_month_input()
    day = get_day_input()
    print('-'*40)
    return city, month, day

def load_bikedata(city, month, day):
    try:
        CSV_COLUMNS = ['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
        df = pd.read_csv(CITY_BIKEDATA[city], usecols=CSV_COLUMNS)
    except FileNotFoundError:
        print(f"Data file for {city} not found. Exiting...")
        exit(1)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.strftime('%A').str.lower()

    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_num]

    if day != 'all':
        df = df[df['Day of Week'] == day]

    return df

def time_stats(df):
    # TO DO: Display statistics on the most frequent times of travel
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Extract month, day of the week, and hour from the 'Start Time' column
    df['Hour'] = df['Start Time'].dt.hour

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print(f"The most common month: {common_month}")

    # Display the most common day of the week
    common_day = df['Day of Week'].mode()[0]
    print(f"The most common day of the week: {common_day}")

    # Display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print(f"The most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Implement station_stats, trip_duration_stats, and user_stats functions in a similar manner

def display_raw_data(df):
    index = 0
    while True:
        raw_data_request = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if raw_data_request.lower() == 'yes':
            print(df.iloc[index:index + 5])
            index += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        # Call station_stats, trip_duration_stats, and user_stats functions here as needed

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

