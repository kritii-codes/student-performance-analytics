import numpy as np
import pandas as pd


#Defining the subjects
SUBJECTS = ['MATH','PYTHON','PHYSICS','JAVA','DSA']


#Deciding the grading rule
def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    elif average >= 50:
        return 'E'
    else:
        return 'F'


#Decides the pass/fail rule
def check_result(row):
    for subject in SUBJECTS:
        if row[subject] < 40:
            return 'Fail'
    return 'Pass'


#Loads the student dataset
def load_data():
    df = pd.read_csv('students.csv')

    required_columns = [
        'Student_ID','NAME','DEPARTMENT','MATH','PYTHON','PHYSICS','JAVA','DSA','ATTENDANCE'
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f'Missing columns: {missing_columns}')

    if df.empty:
        raise ValueError('The student dataset is empty.')

    if df[required_columns].isnull().any().any():
        raise ValueError('The dataset contains missing values.')

    return df


#Calculates each student's performance
def process_data(df):
    df = df.copy()

    df['Total'] = df[SUBJECTS].sum(axis=1)

    df['Average'] = np.mean(df[SUBJECTS].to_numpy(), axis=1)

    df['Grade'] = df['Average'].apply(assign_grade)
    df['Result'] = df.apply(check_result, axis=1)

    return df


# Analyses the class
def analyse_data(df):
    print('\n🦋🦋🦋🦋🦋🦋🦋 STUDENT PERFORMANCE ANALYTICS 🦋🦋🦋🦋🦋🦋🦋')

    print('\n🌺🌺🌺🌺🌺🌺 Student Performance 🌺🌺🌺🌺🌺🌺')
    print(
        df[
            ['Student_ID', 'NAME', 'Total',
             'Average', 'Grade', 'Result']
        ].round({"Average": 2}).to_string(index=False)
    )

    print("\n--- Class Statistics ---")
    print('Total students:', len(df))
    print('Class average:', round(df['Average'].mean(), 2))
    print('Highest average:', round(df['Average'].max(), 2))
    print('Lowest average:', round(df['Average'].min(), 2))

    print('\n🎀🎀🎀🎀🎀🎀 Pass/Fail Statistics 🎀🎀🎀🎀🎀🎀')
    print('Students passed:', (df['Result'] == 'Pass').sum())
    print('Students failed:', (df['Result'] == 'Fail').sum())

    print('\n🌿🌿🌿🌿🌿🌿 Subject-wise Analysis 🌿🌿🌿🌿🌿🌿')
    subject_averages = df[SUBJECTS].mean()

    for subject in SUBJECTS:
        print(
            f'{subject} average: '
            f'{subject_averages[subject]:.2f}'
        )

    best_subject = subject_averages.idxmax()
    print('Best-performing subject:', best_subject)

    print('\n🐦🐦🐦🐦🐦 Top Performers 🐦🐦🐦🐦🐦')
    top_students = df.nlargest(3, "Average")

    print(
        top_students[
            ['NAME', 'Average', 'Grade']
        ].round({'Average': 2}).to_string(index=False)
    )

    print('\n🐵🐵🐵🐵🐵 Attendance Analysis 🐵🐵🐵🐵🐵')
    print(
        'Class average attendance:',
        round(df['ATTENDANCE'].mean(), 2), '%'
    )


# Runs the complete program
def main():
    try:
        students = load_data()
        students = process_data(students)
        analyse_data(students)

    except FileNotFoundError:
        print(
            'Error: students.csv was not found. '
            'Save it beside main.py.'
        )

    except (ValueError, KeyError) as error:
        print('Data error:', error)


if __name__ == '__main__':
    main()


