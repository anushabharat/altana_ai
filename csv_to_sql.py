import pandas as pd
from sqlalchemy import create_engine

# Connects to your local database engine
# [TODO] Please add your postgres db url here
engine = create_engine('postgresql://anushabharat:pass@localhost:5432')
# Read the data and drop the extra empty columns that are created
df=pd.read_csv('data.csv',  on_bad_lines='skip')
df = df.drop(columns = ["Unnamed: 8", "Unnamed: 9", "Unnamed: 10"])
# Convert the dataframe to a table in the database
df.to_sql('company_db', engine)