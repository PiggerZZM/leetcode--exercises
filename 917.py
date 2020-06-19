class Solution:
    def reverseOnlyLetters(self, S):
        s = list(S)
        left = 0
        right = len(s)-1
        while left<right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right] = s[right],s[left]
                left +=1
                right -= 1
            elif not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1

        return ''.join(s)



if __name__ == '__main__':
    string = "Test1ng-Leet=code-Q!"
    s = Solution()
    print(s.reverseOnlyLetters(string))