import pandas as pd
def students_and_examinations(students, subjects, examinations):
    df = students.merge(subjects, how='cross')
    df = df.merge(examinations, on=['student_id', 'subject_name'], how='left')

    result = df.groupby(['student_id', 'student_name', 'subject_name'], as_index=False)['noname'].count()

    return result.rename(columns={'noname':'attended_exams'})