# coding:utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key, l = 0, len(nums)
        while key < l:
            if key + 1 <= l - 1 and nums[key] == nums[key + 1]:
                while key + 2 <= l - 1 and nums[key + 1] == nums[key + 2]:
                    nums.pop(key + 2)
                    l -= 1
            key += 1
        return nums


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))

# 这个题的意思是一个列表里面，取出重复次数超过2的数。例如上面这个，需要返回[0, 0, 1, 1, 2, 3, 3]  我这里的做法时间复杂度不是太高。同时完成了对列表的去重
