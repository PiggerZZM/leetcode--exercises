/*
 * @lc app=leetcode.cn id=150 lang=cpp
 * author: PiggerZZM
 * date: 2020-7-1
 * [150] 逆波兰表达式求值
 */

// @lc code=start
class Solution
{
public:
    bool isdigit(string &str)
    {
        if (str[0] == '-')
            if (str.size() == 1)
                return false;
            else
            {
                for (int i = 1; i < str.size(); i++)
                    if (str[i] > '9' || str[i] < '0')
                        return false;
            }
        else
            for (int i = 0; i < str.size(); i++)
                if (str[i] > '9' || str[i] < '0')
                    return false;
        return true;
    }

    int toint(string &str)
    {
        int result = 0;
        if (str[0] == '-')
        {
            for (int i = 1; i < str.size(); i++)
                result = result * 10 + (str[i] - '0');
            return -result;
        }
        else
        {
            for (int i = 0; i < str.size(); i++)
                result = result * 10 + (str[i] - '0');
            return result;
        }
    }

    int evalRPN(vector<string> &tokens)
    {
        stack<int> s;
        for (int i = 0; i < tokens.size(); i++)
        {
            string str = tokens[i];
            if (isdigit(str))
                s.push(toint(str));
            else
            {
                int num1, num2;
                num2 = s.top();
                s.pop();
                num1 = s.top();
                s.pop();
                if (str == "+")
                    s.push(num1 + num2);
                else if (str == "-")
                    s.push(num1 - num2);
                else if (str == "*")
                    s.push(num1 * num2);
                else if (str == "/")
                    s.push(num1 / num2);
            }
        }
        return s.top();
    }
};
// @lc code=end
