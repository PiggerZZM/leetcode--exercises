/*
 * @lc app=leetcode.cn id=605 lang=cpp
 *
 * [605] 种花问题
 */

// @lc code=start
class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int count = 0;
        for (int i = 0; i < flowerbed.size(); i++)
        {
            if (flowerbed[i] == 0)
            {
                int left = i - 1;
                int right = i + 1;
                if (((left >= 0 && flowerbed[left] == 0) || left == -1) && ((right <= flowerbed.size() - 1 && flowerbed[right] == 0) || right == flowerbed.size()))
                {
                    count++;
                    flowerbed[i] = 1;
                }
            }
        }
        if (count >= n)
            return true;
        else
            return false;
    }
};
// @lc code=end
