class Solution
{
public:
    static bool cmp(vector<int> &person1, vector<int> &person2)
    {
        return (person1[1] - person1[0]) < (person2[1] - person2[0]);
    }

    int twoCitySchedCost(vector<vector<int>> &costs)
    {
        int N = costs.size() / 2;
        int totalPrice = 0;
        sort(costs.begin(), costs.end(), cmp);
        for (int i = 0; i < costs.size(); i++)
        {
            if (i < N)
                totalPrice += costs[i][1];
            else
                totalPrice += costs[i][0];
        }

        return totalPrice;
    }
};