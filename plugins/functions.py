#this is plugins/function file
import requests
import pandas as pd
import sqlalchemy
import psycopg2

def main():
    url = 'https://random-data-api.com/api/cannabis/random_cannabis?size=10'
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url,
              headers=headers)

    with open('file_test.csv', 'w') as f:
        f.write(r.text)
    df = pd.read_json('file_test.csv')
    user = 'user'
    password = 'password'
    host = '127.0.0.1'
    Database_name = 'datamarts'
    db = sqlalchemy.create_engine(
        f'postgres://{user}:{password}@{host}/{Database_name}')
    conn = db.connect()
    df.to_sql(f'name_table', con=conn, if_exists='replace')
