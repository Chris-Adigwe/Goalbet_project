from extract_data import extract_data
from load_db import load_to_db
from transform import transform
from util import get_database_conn
from sqlalchemy import create_engine

def main():
    get_database_conn()
    extract_data()
    transform()
    load_to_db()


main()