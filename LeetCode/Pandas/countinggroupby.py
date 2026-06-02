import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director['new_count'] = actor_director.groupby(['actor_id', 'director_id']).transform('size')

    return actor_director[actor_director['new_count'] >= 3][['actor_id', 'director_id'].drop_duplicates()]