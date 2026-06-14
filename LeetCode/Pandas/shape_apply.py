import pandas as pd
# Best Practice -- use shape[0] : count
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ],
    })

# Basic Solution : use left join (merge), apply () for if-else conditions
def categorize(income):
    if income < 20000: return "Low Salary"
    elif 20000 <= income <= 50000: return "Average Salary"
    else: return "High Salary"

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    accounts['category'] = accounts['income'].apply(categorize)

    counts = accounts.groupby('category').size().reset_index(name='accounts_count')

    df = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']})

    final = df.merge(counts, on='category', how='left')

    final['accounts_count'] = final['accounts_count'].fillna(0).astype(int)


    return final