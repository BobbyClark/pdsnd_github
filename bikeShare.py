import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_of_year = ["january", "february", "march", "april", "may", "june","all"]

week_day = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday","all"]

city_to_choose_from = ['chicago','new york city','washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(str('\nWould you like to explore data from Chicago, New York City, or Washington? Type the complete city name.\n'))
        city = city.lower()
        if city in city_to_choose_from:
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('\nYour input is invalid, try again. Input complete city name, i.e. New York City.\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(str('\nInput a specific month from January to June or enter all. Type of the name of the month, i.e. January.\n'))
        month = month.lower()
        if month in month_of_year:
            break
        else:
            print('\nYour input is invalid, try again. Spell out the month name, i.e. January.\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(str('\nInput a specific day of the week or enter all. Spell out the name of the day, i.e. Monday.\n'))
        day = day.lower()
        if day in week_day:
            break
        else:
            print('\nYour input is invalid, try again. Spell out the name of the day, i.e. Monday.\n')


    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]


    print ("Calculating data for {}...".format(city))
    time.sleep(3)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    time.sleep(3)
    start_time = time.time()
    common_hour = df['hour'].mode()[0]
    month = df['month'].mode()[0]
    months = ['january','february','march','april','may','june']
    common_month = months[month - 1].capitalize()
    common_week = df['day'].mode()[0]

    # TO DO: display the most common month
    print('Most common month:',common_month)
    time.sleep(2)

    # TO DO: display the most common day of week

    print('Most common day of week:',common_week)
    time.sleep(2)

    # TO DO: display the most common start hour
    print('Most common start hour:', common_hour)
    time.sleep(2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time.sleep(2)
    start_time = time.time()
    start=df['Start Station'].mode()[0]
    end=df['End Station'].mode()[0]
    trip= df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)

    # TO DO: display most commonly used start station
    print('Most common start station:',start)
    time.sleep(2)

    # TO DO: display most commonly used end station
    print('\nMost common end station:',end)
    time.sleep(2)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost common trip:')
    print(trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    time.sleep(2)
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    travel_time = np.sum(df['Travel Time'])
    avg_travel_time = np.mean(df['Travel Time'])

    # TO DO: display total travel time
    print('Total travel time:',travel_time)
    time.sleep(2)

    # TO DO: display mean travel time
    print('Average travel time:',avg_travel_time)
    time.sleep(2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    time.sleep(2)
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:')
    print(df['User Type'].value_counts())
    time.sleep(2)

    # TO DO: Display counts of gender
    try:
        print('\nCounts of gender:')
        print(df['Gender'].value_counts())
        time.sleep(2)
    except:
        print('No data available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early= np.min(df['Birth Year'])
        recent= np.max(df['Birth Year'])
        common= df['Birth Year'].mode()[0]
        print('\nEarliest birth year:',int(early))
        print('Most recent birth year:',int(recent))
        print('Most common birth year:',int(common))
    except:
        print('No data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Display 5 lines of raw data used for calculations if specified by user then 5 more if specified"""
    rowIndex = 0

    while True:
        rawData = input('\nWould you like to see the raw data used for calculations? Input yes or no.\n')
        rawData = rawData.lower()
        if rawData == 'no':
            return

        if rawData == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5
            break

        else:
            print('Your input is invalid. Please type yes or no.')

    while True:
        moreData = input('\nWould you like to see more raw data used for calculations? Input yes or no.\n')
        moreData = moreData.lower()
        if moreData == 'no':
            return

        if moreData == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5
            break
        else:
            print('Your input is invalid. Please type yes or no.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
