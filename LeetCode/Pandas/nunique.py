import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df.rename(columns={'subject_id' : 'cnt'}, inplace=True)
    return df

# more pythonic solution
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (teacher.groupby('teacher_id')['subject_id']
            .nunique()     # Group by teacher_id, count unique subject_ids,
            .reset_index(name='cnt')) # rename the resulting column to 'cnt' during reset_index
