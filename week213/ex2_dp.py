class Solution:
    def countVowelStrings(self, n):
        # dp[i][n]为首字母为第i个字母的长度为n的字符串数量
        self.dp = [[0]*n for _ in range(5)]
        for i in range(5):
            self.dp[i][0] = 1
        if n == 1:
            return 5
        
        for col in range(1, n):
            for row in range(5):
                mysum = 0
                for k in range(row, 5):
                    mysum += self.dp[k][col-1]
                self.dp[row][col] = mysum
        
        result = 0
        for j in range(5):
            result += self.dp[j][n-1]
        return result

if __name__ == '__main__':
    s = Solution()
    s.countVowelStrings(33)
    