/*
 * @lc app=leetcode.cn id=1 lang=cpp
 * author: PiggerZZM
 * date: 2020-6-22
 * [1] 两数之和
 */

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> hash;
        vector<int> result;
        hash.clear();
        for (int i = 0; i < nums.size(); i++)
            hash[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++)
        {
            map<int, int>::iterator it = hash.find(target - nums[i]);
            if (it != hash.end() && i != it->second)
            {
                result.push_back(i);
                result.push_back(it->second);
                break;
            }
        }
        return result;
    }
};
// @lc code=end
