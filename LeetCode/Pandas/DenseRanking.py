import pandas as py
def orders_scores(scores: pd.DataFrame) -> pd.DataFrame:

df = scores.copy()

df['rank'] = df['score'].rank(method='dense', ascending=False).astype(int)

return df[['score', 'rank']].sort_values(by='rank')

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}
scores = pd.DataFrame(data)
