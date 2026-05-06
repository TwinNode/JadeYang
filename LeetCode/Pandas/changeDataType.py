import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

  #does not work: students.grade.astype(int)
  #in astype (), there is no ''
  #DataFrame['column name'] = DatFrame['column name'].astype(type)
