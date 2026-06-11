import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    # abc def - capitalize() : Abc def
    # title(): Abc Def
    return users