class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        for i in range(0,2**length):
            s = self.make(length,i)
            re = []
            for ele in range(0,length):
                if s[ele] == '1':
                    re.append(nums[ele])
            result.append(re)
        return result

    def make(self,num,i):
        string = str('0'*(num-len(str(bin(i)[2:])))+bin(i)[2:])
        return string



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6]
    result = s.subsets(nums)

