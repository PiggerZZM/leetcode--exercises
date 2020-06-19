/*
author: PiggerZZM
date: 2020-6-19
language: cpp
*/

class SolutionB {
public:
    int maxProfit(vector<int>& prices) {
        // minPrice记录第i天之前的最低价
        int minPrice = 1e9;
        int maxProfit = 0;
        for (int i=0; i<prices.size(); i++) {
            minPrice = min(minPrice, prices[i]);
            maxProfit = max(maxProfit, prices[i]-minPrice);
        }
        return maxProfit;
    }
};