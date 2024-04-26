import pandas as pd

def timeSeries(initial_df, column):
    initial_df['Timestamp'] = pd.to_datetime(initial_df['Timestamp'])
    ts_indexed_df = initial_df.loc[:, ['Timestamp', column]]
    ts_indexed_df.set_index('Timestamp',inplace=True)
    monthly_data =ts_indexed_df.resample('ME').mean()
    return monthly_data