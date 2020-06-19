class SolutionA {
public:
    int maxProfit(vector<int>& prices) {
        // dp[i]表示第i天卖出时最大利润，用辅助变量minPrice记录当前最小price
        vector<int> dp;
        int maxProfit = 0;
        int minPrice = 1e9;
        for (int i=0; i<prices.size(); i++) {
            if (prices[i] < minPrice)
                minPrice = prices[i];
            if (i == 0)
                dp.push_back(0);
            else {
                int temp = max(dp[i-1], prices[i] - minPrice);
                dp.push_back(temp);
                if (temp > maxProfit)
                    maxProfit = temp;
            }
        }
        return maxProfit;
    }
};