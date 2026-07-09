import pandas as pd
import numpy as np

reviews = pd.DataFrame({
    'review_id':     [1, 2, 3, 4, 5, 6, 7],
    'product_id':    [101, 101, 101, 102, 102, 103, 103],
    'rating':        [4.0, 5.0, 3.0, 4.5, np.nan, 2.0, 3.0],
    'helpful_votes': [10, np.nan, 5, 3, 2, 0, 1]
})

def product_review_summary(reviews: pd.DataFrame) -> pd.DataFrame:
    #df = reviews.copy()

    # df['review_count'] = df.groupby('product_id')['rating'].sum()
    # df['avg_rating'] = df.groupby('product_id')['rating'].mean().round(2)

    final = reviews.groupby('product_id').agg(
        review_count = ('rating', len), # count는 결측값 제외 갯수, len/size는 결측값 포함 갯수
        avg_rating = ('rating', 'mean'),
        total_helpful = ('helpful_votes', 'sum')
    ).reset_index().round({'avg_rating': 2}).astype({'total_helpful': int})

    #final['avg_rating'] = final['avg_rating'].round(2)

    columns = ['product_id', 'review_count', 'avg_rating', 'total_helpful']
    return final[columns].sort_values('product_id').reset_index(drop=True)


result = product_review_summary(reviews)
print(result)
print(result.dtypes)