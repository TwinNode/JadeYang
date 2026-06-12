import pandas as pd
def find_patients(patients: pd.DataFrame) => pd.DataFrame:
    return patients[patients['conditions'].str.contrains(r'(^|\s+)DIAB1')]
# (r'(^|\s)DIAB1') is same as (r'(^DIAB1) | (\sDIAB1)')
# ^(DIAB1) starts with DIAB1
# | or (\sDIAB1) there is spacing before DIAB1
# \s+ at least more than one spacing