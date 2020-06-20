/*
author: PiggerZZM
date: 2020-6-20
language: cpp
*/

class Solution {
public:
    int minFlipsMonoIncr(string S) {
        int len = S.size();
        if (len == 0)
            return 0;
        
        // dp[i]定义为01分割点在S[i-1]和S[i]之间时需要的最小翻转次数
        vector<int> dp;
        int count = 0;

        // 0的总数就是dp[0]
        for (int i=0; i<len; i++) {
            if (S[i] == '0')
                count++;
        }
        dp.push_back(count);

        int result = count;
        for (int i=1; i<=len; i++) {
            if (S[i-1] == '1')
                dp.push_back(dp[i-1] + 1);
            else
                dp.push_back(dp[i-1] - 1);
            result = min(result, dp[i]);
        }
        return result;
    }
};