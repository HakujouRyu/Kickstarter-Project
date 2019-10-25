import os
import pandas as pd
import numpy as np
import json


def get_all_csv():
    """Gets all of the csv files from all the different directories and concatenates them together
    into one big DataFrame WARNING: This will create a large df! Shape(4+mill, 37)"""
    whole = pd.DataFrame(
            columns=['backers_count', 'blurb', 'category', 'converted_pledged_amount',
       'country', 'created_at', 'creator', 'currency', 'currency_symbol',
       'currency_trailing_code', 'current_currency', 'deadline',
       'disable_communication', 'fx_rate', 'goal', 'id', 'is_starrable',
       'launched_at', 'name', 'photo', 'pledged', 'profile', 'slug',
       'source_url', 'spotlight', 'staff_pick', 'state', 'state_changed_at',
       'static_usd_rate', 'urls', 'usd_pledged', 'usd_type', 'location',
       'friends', 'is_backing', 'is_starred', 'permissions']
    )
    parents = os.listdir('Data')  #Get the Yearly folders inside the Data folder
    for parent in parents:  
        folders = os.listdir(f'Data\\{parent}') #Get the monthly folders inside the yearly folders
        for folder in folders:
            files = os.listdir(f'Data\\{parent}\\{folder}')  #Get the filenames inside monthly folders
            monthly = pd.concat(
                [pd.read_csv(
                    f'Data\\{parent}\\{folder}\\{file}'
                            ) for file in files]
            ) #Reads in all the csv files in a given month
            whole = whole.append(monthly) #Appends the monthly df to the whole
    return whole
            # Seems to work, but is too large for my computer to handle. 
            # I'll use some logic from it to get yearly files to work with for now


def get_a_year(year):
    """ Grabs all files for the year provided """
    df = pd.DataFrame(
            columns=['backers_count', 'blurb', 'category', 'converted_pledged_amount',
       'country', 'created_at', 'creator', 'currency', 'currency_symbol',
       'currency_trailing_code', 'current_currency', 'deadline',
       'disable_communication', 'fx_rate', 'goal', 'id', 'is_starrable',
       'launched_at', 'name', 'photo', 'pledged', 'profile', 'slug',
       'source_url', 'spotlight', 'staff_pick', 'state', 'state_changed_at',
       'static_usd_rate', 'urls', 'usd_pledged', 'usd_type', 'location',
       'friends', 'is_backing', 'is_starred', 'permissions']
    )
    folders = os.listdir(f'Data\\{year}') #Get the monthly folders inside the year
    for folder in folders:
        files = os.listdir(f'Data\\{year}\\{folder}')  #Get the filenames inside monthly folders
        monthly = pd.concat(
            [pd.read_csv(
                f'Data\\{year}\\{folder}\\{file}') for file in files]
        ) #Reads in all the csv files in a given month
        df = df.append(monthly)
        df = df.reset_index().drop(columns='index')
    return df


def get_a_few(year):
    """ Grabs a few files from the year provided """ 
    df = pd.DataFrame(
            columns=['backers_count', 'blurb', 'category', 'converted_pledged_amount',
       'country', 'created_at', 'creator', 'currency', 'currency_symbol',
       'currency_trailing_code', 'current_currency', 'deadline',
       'disable_communication', 'fx_rate', 'goal', 'id', 'is_starrable',
       'launched_at', 'name', 'photo', 'pledged', 'profile', 'slug',
       'source_url', 'spotlight', 'staff_pick', 'state', 'state_changed_at',
       'static_usd_rate', 'urls', 'usd_pledged', 'usd_type', 'location',
       'friends', 'is_backing', 'is_starred', 'permissions']
    )
    folders = os.listdir(f'Data\\{year}') #Get the monthly folders inside the year
    for folder in folders[:1]: #Grab a folder from that year
        files = os.listdir(f'Data\\{year}\\{folder}')  #Get the filenames inside monthly folders
        monthly = pd.concat(
            [pd.read_csv(
                f'Data\\{year}\\{folder}\\{file}') for file in files[:1]] #Grab a file
        ) #Reads in all the csv files in a given month
        df = df.append(monthly)
        df = df.reset_index().drop(columns='index')
    return df


def datetime_convert(df):
    """ Converts ['created_at', 'dealdine', 'launched_at'] into pandas.dt, 
        and creates columns for month day and year.
        Also creates 'days_to_launch' and 'campaign_length' columns """
    #Time is in seconds (epoch)
    df['created_at'] = pd.to_datetime(df['created_at'], unit='s')
    df['deadline'] = pd.to_datetime(df['deadline'], unit='s')
    df['launched_at'] = pd.to_datetime(df['launched_at'], unit='s')
    # df['state_changed_at'] = pd.to_datetime(df['state_changed_at'], unit='s') Leakage for current project goals

    #Break time up into columns Month day etc
    df['month_started'] = df['created_at'].dt.month
    df['day_started'] = df['created_at'].dt.weekday
    df['year_started'] = df['created_at'].dt.year
    df['month_launched'] = df['launched_at'].dt.month
    df['day_launched'] = df['launched_at'].dt.weekday
    df['year_launched'] = df['launched_at'].dt.year
    df['deadline_month'] = df['deadline'].dt.month
    df['deadline day'] = df['deadline'].dt.weekday
    df['deadline_year'] = df['deadline'].dt.year

    #Feature engineering
    df['days_to_launch'] = (df['launched_at'] - df['created_at']).dt.days
    df['campaign_length'] = (df['deadline'] - df['launched_at']).dt.days #campaign length in days
    
    return df

def time_to_string(df):
    """  Convert back into strings so that we can pass to model """    
    df['created_at'] = df['created_at'].astype(str)
    df['deadline'] = df['deadline'].astype(str)
    df['launched_at'] = df['launched_at'].astype(str)
    df['state_changed_at'] = df['state_changed_at'].astype(str)

    return df


def col_dict(df, col):
    #ONLY WORKS WITH 'category' AS IS!
    # So I removed the for loop for now
    """Takes in a DataFrame and a list of column
    names and unpacks the 'dictionaries' into new columns """
        #for col in cols: #Loop over columns
    df[col] = df[col].apply(json.loads)
    df_of_column = df[col].apply(pd.Series)
    df_of_column.columns = [f'{col}_'+col_name for col_name in df_of_column.columns]
    df = df.join(df_of_column)
    return df.drop(columns=col)


def drop_dupes(df):
    """ Drops rows that are duplicate projects """
    df = df[~df.duplicated('id')]
    df = df.reset_index().drop(columns='index')
    return df


    # I only care about these two states for now
def completed_campaigns(df):
    """ Reurns only rows with 'state' 'failed' or 'success' """
    df = df[df['state'].isin(['failed', 'successful'])]
    return df



if __name__ == "__main__":
    import os
    import pandas as pd
    import numpy as np
    import json