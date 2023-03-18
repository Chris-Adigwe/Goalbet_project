import pandas as pd
import numpy as np
from util import get_database_conn
from sqlalchemy import create_engine
from dotenv import dotenv_values


def load_to_db():
    engine = get_database_conn()
    print(engine)
    df= pd.read_csv('Goalbet_project/data/transformed_file.csv') # Read csv file
    df.to_sql('GoalBet', con= engine, if_exists='replace', index= False)
    print('Data successfully written to PostgreSQL database')
