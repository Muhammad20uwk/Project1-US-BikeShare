import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input("choose city of (chicago, new york city, washington) to get data.\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid, please try again")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        
        month = input("choose month of (January, February, march, april, may, June) or (All). \n").lower()
        if month.lower() in months:
            break
        else:
            print("Invalid, please try again")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        
        day = input("choose one of weekdays ( monday, tuesday, ...etc ) or All \n").lower()

        if day.lower() in days:
            break
        else:
            print("Invalid , please try again")


    print('-'*40)


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

    # extract month , hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
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
        days = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday']
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of week is: {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is: {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The  most commonly used start station is: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The  most commonly used end station is: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df['Start Station'] + " and " +  df['End Station']

    print("The  most frequent combination of start and end station trip is: {}".format(start_end_station.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: {}".format(df['Trip Duration'].sum()))
    # TO DO: display mean travel time
    print("Average travel time: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    print("counts of user types:\n {}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if city != 'washington':
        
        print("counts of gender:\n {}".format(df['Gender'].value_counts()))
    
    # TO DO: Display the earliest year of birth
        print("The earliest year of birth is: {}".format(df['Birth Year'].min()))
   
    # TO DO: Display the most recent year of birth
        print("The most recent year of birth is: {}".format(df['Birth Year'].max()))
    
    # TO DO: Display the most common year of birth
        print("The most common year of birth is: {}".format(df['Birth Year'].mode()[0]))
    
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the City Data')
        print('Birth stats cannot be calculated because Birth Year does not appear in the City Data')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    response = ['yes','no']

    while True:
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no? \n').lower()
        if view_data in response:
            if view_data=='yes':
                start_loc = 0
                print(df.iloc[start_loc:start_loc + 5])
            break     
        else:
            print("Invalid , please try again")
            
    while True:
        view_display= input('Do you wish to continue? Enter yes or no? \n').lower()
        if view_display in response:
            if view_display=='yes':
                start_loc += 5
                print(df.iloc[start_loc:start_loc + 5])
            else:    
                break  
        else:
            print("Invalid , please try again")       
            
 
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart not in  ['yes' , 'no']:
            print('Invalid , Please Enter Yes or No')
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        elif restart != 'yes':
            break


if __name__ == "__main__":
	main()
