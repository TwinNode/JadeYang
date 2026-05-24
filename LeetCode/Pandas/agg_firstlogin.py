import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='event_date', inplace=True)

    df = activity[['player_id', 'event_date']].copy()
    df['first_login'] = df.groupby(['player_id'])['event_date'].transform('min')

    return df[['player_id', 'first_login']].drop_duplicates()

#use aggregation
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id').agg(first_login=('event_date', 'min)).reset_index()
