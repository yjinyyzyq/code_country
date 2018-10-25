# coding:utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int(len(nums)*(1+len(nums))/2 - sum(nums))

print(Solution().missingNumber([0, 1, 2, 3]))

# 这个题目的意思是给你一个从0开始的数组，你要找到它不连续的地方，确实的那个数。比如[1,2,3]。这里缺失的就是0.如果是[0,1,2,3]缺失的就是4.