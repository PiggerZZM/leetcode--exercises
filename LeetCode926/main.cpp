/*
author: PiggerZZM
date: 2020-6-20
language: cpp
*/

#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

#include "LeetCode926.cpp"

int main()
{
    Solution s;
    string mystr = "100000001010000";
    int result = s.minFlipsMonoIncr(mystr);
    printf("%d\n", result);

    return 0;
}