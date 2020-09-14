class Solution
{
public:
    int numSpecial(vector<vector<int>> &mat)
    {
        int rows = mat.size();
        int cols = mat[0].size();
        int count = 0;
        bool flag;
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                if (mat[row][col] == 1)
                {
                    flag = true;
                    for (int i = 0; i < rows; i++)
                    {
                        if (i == row)
                            continue;
                        else
                        {
                            if (mat[i][col] == 1)
                            {
                                flag = false;
                                break;
                            }
                        }
                    }
                    if (flag)
                    {
                        for (int j = 0; j < cols; j++)
                        {
                            if (j == col)
                                continue;
                            else
                            {
                                if (mat[row][j] == 1)
                                {
                                    flag = false;
                                    break;
                                }
                            }
                        }
                    }
                    if (flag)
                        count++;
                }
            }
        }
        return count;
    }
};
