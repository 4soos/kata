from typing import List


class Solution:
    """
    state transformation function:
                    | Ⅰ  grid[i, j]               , i = 0, j = 0
                    | Ⅱ  grid(i,j)+dp(i,j−1)      , i = 0, j != 0
        dp[i][j] ===|  
                    | Ⅲ grid(i,j)+dp(i,j−1)      , i != 0, j = 0
                    | Ⅳ grid(i,j)+dp(i,j−1)      , i != 0, j != 0

    Args:
        grid: two-dimensional array

    Returns:
        a (int) value  

    """
    def __init__(self) -> None:
        pass

    def max_values(self, grid: List[List[int]]) -> int:
  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # Ⅰ
                if i == 0 and j == 0: continue

                # Ⅱ
                if i == 0: grid[i][j] += grid[i][j-1]

                # Ⅲ
                elif j == 0: grid[i][j] += grid[i - 1][j]

                # Ⅳ
                else: grid[i][j] += max(grid[i][j - 1], grid[i-1][j])

        return grid[-1][-1]
