## TODO: import all necessary packages and functions
import csv
import datetime
from pprint import pprint
import pandas as pd
import numpy as np
import time

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

city_dict={"Chicago":chicago,"New York": new_york_city,"Washington":washington} ## mapping city-city file


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    try:
        city=city_dict.get(city)  ##we need to return not the city name, but name of the file
        return(city)
    except:
        raise ValueError("Only values \"Washington\", \"New York\" and \"Chicago\" are accepted") ## you want to return error if you receive unexpected value

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    if time_period not in ["none","month","day"]:
        raise ValueError("Only values \"none\",\"month\",\"day\" are accepted") ## you want to return error if you receive unexpected value
    else:
        return(time_period)
  
def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    if month not in ["January","February", "March", "April", "May","June"]:
        raise ValueError("Only values \"January\",\"February\", \"March\", \"April\", \"May\", \"June\" are accepted") ## you want to return error if you receive unexpected value
    else:
        return(month)


def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    if day not in [x+1 for x in range(31)]:
        raise ValueError("Only integer from 1 to 31 is accepted")
    else:
        return(day)


def popular_month(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B') ## like that you get month names right away
    popular_month = df['month'].mode()[0]
    return('Popular Month:', popular_month)

def popular_day(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.strftime('%A') ## like that you get week days right away
    popular_day = df['day'].mode()[0]
    return('Popular Day:', popular_day)

def popular_hour(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    return('Popular Hour:', popular_hour)


def trip_duration(city_file, day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day'] = df['Start Time'].dt.day
    ## filter out the date
    if month!='all':
        df = df[df['month']==month]
    if day!='all':
        df = df[df['day'] == day]
    total = np.sum(df['Trip Duration'])
    average = np.average(df['Trip Duration'])
    return (total, average)

                      
def popular_stations(city_file,  day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function, repeat the same filtering  as for trip_duration
    df = pd.read_csv(city_file)
    start_station = df['Start Station'].value_counts().index[0] ## you need a name, not pandas Series as output
    end_station = df['End Station'].value_counts().index[0] ## you need a name, not pandas Series as output
    ## you could do mode here as well!!!
    return (start_station, end_station)
    


def popular_trip(city_file, day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    ## trip definition: combination of start station & end station
    df = pd.read_csv(city_file)
    df['trip'] = df['Start Station']+'-'+df['End Station']
    ## compute mode as before
    # TODO: complete function, repeat the same filtering  as for trip_duration


def users(city_file, day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function,  repeat the same filtering  as for trip_duration
    df = pd.read_csv(city_file)
    user_types = df['User Type'].value_counts()
    return(user_types)


def gender(city_file, day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function,  repeat the same filtering  as for trip_duration
    df = pd.read_csv(city_file)
    gender = df['Gender'].value_counts()
    return(gender)


def birth_years(city_file, day, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function,  repeat the same filtering  as for trip_duration
    df = pd.read_csv(city_file)
    oldest = df['Birth Year'].min()
    youngest = df['Birth Year'].max()
    avg = df['Birth Year'].mean()
    print('Oldest user born in:', min, " ", 'Youngest user born in:', max, " ", 'Average user birth year:',avg)


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    return(display)


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        month='all'
        day='all'
    if time_period == 'month':
        month=get_month()
        day='all'
    if time_period == 'day':
        month=get_month()
        day=get_day()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month(city)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city, day, month)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
    