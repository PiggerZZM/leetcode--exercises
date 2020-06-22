# @author: PiggerZZM
# @lc app=leetcode.cn id=1 lang=python3
# @date: 2020-6-22
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for index, value in enumerate(nums):
            if target - value in hash_map and hash_map[target - value] != index:
                result.append(index)
                result.append(hash_map[target - value])
                break

        return result
# @lc code=end
