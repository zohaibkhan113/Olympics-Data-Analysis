import pandas as pd

def preprocess():
    df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Datasets/athlete_events.csv")
    region_df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Datasets/noc_regions.csv")

    # Filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    # Rename region_df columns
    region_df = region_df.rename(columns={
        'Bronze': 'Bronze_region',
        'Gold': 'Gold_region',
        'Silver': 'Silver_region'
    })

    # Merge the two DataFrames
    df = pd.merge(df, region_df, on='NOC', how='left', suffixes=('', '_region'))

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # One-hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df
