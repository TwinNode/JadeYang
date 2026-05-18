import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame)-> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id')
    df= df.rename(columns={'name_y':'Department', 'name_x':'Employee'})
    df = df[['Department', 'Employee', 'salary']]
    maxsalary = df.groupby('Department').salary.transform('max') # Use transform('max') to bring all information that has max salary in each dept.
    df = df[df['salary']==maxsalary]
    return df

#more pythonic way
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame)-> pd.DataFrame:
    df = employee.merge(
        department[['id', 'name']],
        left_on = 'departmentId',
        right_on = 'id',
        suffixes=('_emp','_dept')
    )

    df = df.rename(columns={'name_dept' : 'Department',
                   'name_emp' : 'Employee', 'salary':'Salary'})
    
    isHighestSalary = df['Salary'] == df.groupby('Department')['Salary'].transform('max')

    return df.loc[isHighestSalary, ['Department', 'Employee', 'Salary']]




data1 = {
    'id': [1,2,3,4,5],
    'name' : ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary' : [70000, 90000, 80000, 60000, 90000],
    'departmentId' : [1,1,2,2,1]
         }

data2 = {
    'id' : [1,2],
    'name' : ['IT', 'Sales']
}

employee = pd.DataFrame(data1)
department = pd.DataFrame(data2)

department_highest_salary(employee,department)
