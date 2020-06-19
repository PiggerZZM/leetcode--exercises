#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

#include "LeetCode121-a.cpp"
#include "LeetCode121-b.cpp"

int main()
{
    SolutionA s1;
    vector<int> prices = {7,1,5,3,6,4};
    int result = s1.maxProfit(prices);
    printf("%d\n", result);

    SolutionB s2;
    result = s2.maxProfit(prices);
    printf("%d\n", result);
    
    return 0;
}