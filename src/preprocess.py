import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def filter_india(df):
    df = df[df['location'] == 'India']
    df['date'] = pd.to_datetime(df['date'])
    return df