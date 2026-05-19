import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        grid = np.array(grid)
        grid_t = grid.transpose()
     
        for x in grid:
            for y in grid_t:
                if (x == y).all():
                    count += 1
        return count

#better performance, speed    
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        #가로줄이 리스트라 딕셔너리 키로 못 쓰므로 tuple로 변환하여 갯수를 셈
        #Counter의 key로 쓰려면(딕셔너리 키도 동일) 불변해야 함
        count = 0
        for col in zip(*grid):
        #zip(*grid)는 중첩세로문 없이 세로줄만 뽑아낼 수 있음
            count += row_counts[col]
            #만약 row_counts의 튜플에 똑같은 모양이 있다면 +1
        
        return count

#Use pandas
import pandas as pd
class Solution:
    def equalPairs(self, grid):
        df_row = pd.DataFrame(grid)
        df_col = pd.DataFrame(grid).transpose()

        merged = df_row.merge(df_col, how='inner')

        return len(merged)
        
                
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
sol = Solution()
sol.equalPairs(grid)
