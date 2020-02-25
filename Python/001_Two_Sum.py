# coding: utf-8
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

from typing import List

class Solution:
    # 朴素暴力
    def twoSumBySimple(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            a = nums[i]
            for j in range (i+1, len(nums)):
                if a + nums[j] == target:
                    return [i, j]
        return None

    #hash 1
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     lookup = {}
    #     for i, num in enumerate(nums):
    #         lookup[num] = i

    #     for i, num in enumerate(nums):
    #         complement = target - num
    #         if complement in lookup and i != lookup[complement]:
    #             return [i, lookup[complement]]
    #     return None

    # #hash 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [i, lookup[complement]]
            lookup[num] = i
        return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
