class Solution
{
public:
    int unhappyFriends(int n, vector<vector<int>> &preferences, vector<vector<int>> &pairs)
    {
        // 记录每个人的当前配对朋友
        map<int, int> myfriend;
        int count = 0;
        for (int i = 0; i < pairs.size(); i++)
        {
            myfriend[pairs[i][0]] = pairs[i][1];
            myfriend[pairs[i][1]] = pairs[i][0];
        }

        // 用来标记不开心的人
        map<int, bool> unhappy;
        for (int x = 0; x < preferences.size(); x++)
        {
            for (int uIndex = 0; uIndex < index(preferences, x, myfriend[x]); uIndex++)
            {
                // 遍历可能使x不开心的人u
                int u = preferences[x][uIndex];
                if (index(preferences, u, x) < index(preferences, u, myfriend[u]))
                {
                    // 满足不开心条件则标记
                    unhappy[u] = true;
                    unhappy[x] = true;
                }
            }
        }

        return unhappy.size();
    }

    // 找出a亲近列表下b的下标
    int index(vector<vector<int>> &preferences, int a, int b)
    {
        int i;
        for (i = 0; i < preferences[a].size(); i++)
        {
            if (preferences[a][i] == b)
                break;
        }
        return i;
    }
};