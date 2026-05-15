import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    output = views.loc[views.author_id == views.viewer_id].drop_duplicates(subset=['author_id', 'viewer_id'])
    output = output.rename(columns = {'author_id' : 'id'}).sort_values(by='id')
    return output[['id']] 

#better solution
def article_views(views: pd.DataFrame) -> pd.DataFrame:

    ids = sorted(views.loc[views['author_id'] == views['viewer_id'], 'author_id'].unique()) # to numpy array
    
    return pd.DataFrame({'id': ids}) #new name
