import pandas as pd
import numpy as np

students = pd.DataFrame({
    'student_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Carol', 'Dave']
})

enrollments = pd.DataFrame({
    'student_id': [101, 101, 101, 102, 102, 103, 103],
    'course_id':  ['C1', 'C2', 'C4', 'C1', 'C3', 'C2', 'C3'],
    'score':      [85, 45, 99, 90, 55, np.nan, 78],
    'status':     ['completed', 'completed', 'dropped', 'completed', 'completed', 'completed', 'completed']
})

courses = pd.DataFrame({
    'course_id': ['C1', 'C2', 'C3'],
    'credit': [3, 4, 2]
})

def create_student_features(students: pd.DataFrame, enrollments: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:

    df = courses.merge(enrollments[enrollments['status'] != 'dropped'], on ='course_id', how='left')
    
    df['pass'] = (df['score'] >= 60).astype(int)


    res = df.groupby('student_id').agg(
        courses_taken = ('course_id', 'count'),
        avg_score = ('score', 'mean'),
        total_credits = ('credit', 'sum'),
        pass_count = ('pass', 'sum')
    ).reset_index()
    
    res['pass_rate'] = (res['pass_count'] / res['courses_taken']).round(2)

    final = students.merge(res, how='left', on='student_id').fillna(0).astype({'courses_taken': int, 'total_credits': int})
    
    return final[['student_id', 'name', 'courses_taken', 'avg_score', 'total_credits', 'pass_rate']].sort_values('student_id').reset_index(drop=True)



result = create_student_features(students, enrollments, courses)
print(result)

def test_create_student_features():
    expected = pd.DataFrame({
        'student_id': [101, 102, 103, 104],
        'name': ['Alice', 'Bob', 'Carol', 'Dave'],
        'courses_taken': [2, 2, 2, 0],
        'avg_score': [65.0, 72.5, 78.0, 0.0],
        'total_credits': [7, 5, 6, 0],
        'pass_rate': [0.5, 0.5, 0.5, 0.0]
    })
    out = create_student_features(students, enrollments, courses).reset_index(drop=True)
    pd.testing.assert_frame_equal(out, expected, check_dtype=False)
    print("PASS")

test_create_student_features()

# better practice : use assign
def create_student_features(students: pd.DataFrame, enrollments: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
    completed = (
        enrollments[enrollments['status'] == 'completed']
        .merge(courses, on='course_id', how='left')
        .assign(passed=lambda d: (d['score'] >= 60).astype(int))
    )

    summary = completed.groupby('student_id').agg(
        courses_taken=('course_id', 'count'),
        avg_score=('score', 'mean'),
        total_credits=('credit', 'sum'),
        passed_count=('passed', 'sum'),
    ).reset_index()
    summary['pass_rate'] = (summary['passed_count'] / summary['courses_taken']).round(2)
    summary['avg_score'] = summary['avg_score'].round(2)

    final = (
        students.merge(summary, on='student_id', how='left')
        .fillna(0)
        .astype({'courses_taken': 'int64', 'total_credits': 'int64'})
    )

    cols = ['student_id', 'name', 'courses_taken', 'avg_score', 'total_credits', 'pass_rate']
    return final[cols].sort_values('student_id').reset_index(drop=True)