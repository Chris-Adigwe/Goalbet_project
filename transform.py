import pandas as pd
import numpy as np

# Data load transform and load layer
def transform():
    col_names = ['Div','Date','Time','HomeTeam','AwayTeam','FTHG','FTAG']
    df= pd.read_csv('Goalbet_project/data/file.csv',usecols=col_names) # Read csv file
    if df['Time'].isna().any():
        # Fill the missing values with the mean value
        mean_time = df['Time'].mean()
        df['Time'] = df['Time'].fillna(mean_time)
        df['Date'] = pd.to_datetime(df['Date'])

    df.to_csv('Goalbet_project/data/transformed_file.csv', index= False)