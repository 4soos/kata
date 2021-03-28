#include <vector>

class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        // 初始化第一行
        for(int j=1; j < n; j++) grid[0][j] += grid[0][j - 1];

        // 初始化第一列
        for(int i=1; i < m; i++) grid[i][0] += grid[i - 1][0];

        for(int i=1; i < m; i++)
            for(int j=1; j < n; j++) {
                grid[i][j] += max(grid[i][j-1], grid[i-1][j]);
            }
        
        return grid[m - 1][n - 1];

    }    
};