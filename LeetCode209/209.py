class Solution:
    def minSubArrayLen(self, s, nums):
        sum = 0
        result = len(nums)
        flag = 0
        for index in range(0, len(nums)):
            sum = 0
            for index1 in range(index, min(index + result, len(nums))):
                if nums[index1] + sum >= s:
                    if index1 - index < result:
                        result = index1 - index + 1
                        flag = 1
                    break
                sum += nums[index1]
                if not flag:
                    result = 0
        return result


if __name__ == '__main__':
    s = Solution()
    n = 4
    nums = [1, 4, 4]
    print(s.minSubArrayLen(n, nums))
