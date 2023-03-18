import pandas as pd
import numpy as np

# Data Extraction layer
def extract_data():
    table_data = []
    url=['https://www.football-data.co.uk/mmz4281/1920/E0.csv','https://www.football-data.co.uk/mmz4281/1920/E2.csv','https://www.football-data.co.uk/mmz4281/0203/E1.csv']
    for i in url:
        df = pd.read_csv(i, on_bad_lines='skip')
        if 'Time' not in df.columns:
            df.insert(0, 'Time', pd.Timestamp.now())
        table_data.append(df)
    df = pd.concat(table_data)
    df.to_csv('Goalbet_project/data/file.csv', index= False)