import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "F:\computer_science\data_science\my_projects\\bikeshare_US\chicago.csv",
              'new york city': 'F:\computer_science\data_science\my_projects\\bikeshare_US\\new_york_city.csv',
              'washington': 'F:\computer_science\data_science\my_projects\\bikeshare_US\washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

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
        city=input("dear user, please told me the city you want to explore it : chicago , new york city or washington ? \n").lower()
        if city in CITIES:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("now choose which month you want to explor it : \n monthes : ('january', 'february', 'march', 'april', 'may', 'june') \n or     say 'all' to apply no filter on monthes")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("ok this the last thing, tell me which day of week you want or again say 'all' to apply no filter on days")


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
    #loading data into dataframe
    df=pd.read_csv(CITY_DATA[city])
    #to filter df by month and day we must covert start time column to datetime then extarct month ad day column from it
    #covert start time to datetime
    df["Start Time"]=pd.to_datetime(df['Start Time'])
    #to extract month and day columns
    df["month"]=df["Start Time"].dt.month

    df["day_of_week"]=df["Start Time"].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    #filtering by month and day
    if month !='all':
        monthes=['january', 'february', 'march', 'april', 'may', 'june']
        month=monthes.index(month)+1

        df=df[df['month']==month]

    if day != 'all':
         df = df[df['day_of_week'] == day.title()]

    df["day"]=df["Start Time"].dt.day_name()

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is : \n",df["month"].value_counts().idxmax())


    # TO DO: display the most common day of week
    print("The most common day of week is : \n",df["day_of_week"].value_counts().idxmax())


    # TO DO: display the most common start hour
    print("The most common start hour is : \n",df["hour"].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is : \n",df["Start Station"].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("The most commonly used end station is : \n",df["Start Station"].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=df[["Start Station","End Station"]].mode().loc[0]
    print("the most common combination of start and end station is : \n",most_common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time is : \n",df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("Mean travel time is : \n",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types : \n",df["User Type"].value_counts())


    # TO DO: Display counts of gender
    if "gender" in df.columns:
        print("counts of gender : \n",df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("the earlist year of birth is : \n",df["Birth Year"].min())
        print("\n the most recent year of birth is : \n",df["Birth Year"].max())
        print("\n the most common year of birth is : \n",df["Birth Year"].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thanks for your time")
            break


if __name__ == "__main__":
	main()
