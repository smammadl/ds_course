%pip install sqlalchemy psycopg2-binary

from sqlalchemy import create_engine
import pandas as pd

username = 'username'
password = 'password'
host = 'host'
database = 'world'

engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')

table_name = 'country'
df_table = pd.read_sql_table(table_name, con=engine)
df_table