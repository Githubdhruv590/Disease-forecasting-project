def create_features(df):
    df['lag_1'] = df['new_cases'].shift(1)
    df['lag_7'] = df['new_cases'].shift(7)
    df['lag_14'] = df['new_cases'].shift(14)
    df['rolling_avg'] = df['new_cases'].rolling(7).mean()
    df = df.dropna()
    return df