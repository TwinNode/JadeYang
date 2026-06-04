import pandas as pd
def students_and_examinations(students, subjects, examinations):
    df = students.merge(subjects, how='cross')
    count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    result = df.merge(count, on=['student_id', 'subject_name'], how='left')

    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    return result.sort_values(by=['student_id', 'student_name', 'subject_name'])