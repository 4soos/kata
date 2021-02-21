// LT 766 托普利茨矩阵

class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>> &matrix)
    {
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (matrix[i][j] != matrix[i - 1][j - 1])
                {
                    return false;
                }
            }
        }
        return true;
    }
};

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize, n = matrixColSize[0];
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] != matrix[i - 1][j - 1]) {
                return false;
            }
        }
    }
    return true;
}

