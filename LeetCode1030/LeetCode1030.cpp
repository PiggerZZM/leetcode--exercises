/*
 * @lc app=leetcode.cn id=1030 lang=cpp
 *
 * author: PiggerZZM
 * date: 2020-6-23
 * [1030] 距离顺序排列矩阵单元格
 */

// @lc code=start
class Solution
{
public:
    int visit[110][110];
    int X[4] = {0, 0, -1, 1};
    int Y[4] = {1, -1, 0, 0};

    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0)
    {
        vector<vector<int>> result;
        memset(visit, 0, sizeof(visit));
        queue<pair<int, int>> q;
        q.push({r0, c0});
        visit[r0][c0] = 1;
        while (!q.empty())
        {
            pair<int, int> top = q.front();
            q.pop();
            int tempR = top.first;
            int tempC = top.second;

            vector<int> currentPoint = {tempR, tempC};
            result.push_back(currentPoint);
            
            for (int i = 0; i < 4; i++)
            {
                int nextR = tempR + X[i];
                int nextC = tempC + Y[i];
                if (nextR >= 0 && nextR < R && nextC >= 0 && nextC < C && !visit[nextR][nextC])
                {
                    q.push({nextR, nextC});
                    visit[nextR][nextC] = 1;
                }
            }
        }

        return result;
    }
};
// @lc code=end
