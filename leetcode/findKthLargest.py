# coding:utf-8
class Solution(object):

    def partition(self, nums, start, end):
        if end <= start:
            return
        base = nums[start]
        while start < end:
            while start < end and nums[end] >= base:
                end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] <= base:
                start += 1
            nums[end] = nums[start]
        nums[start] = base
        return start

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        if not nums or k <= 0 or k > l:
            return
        start = 0
        end = l - 1
        index = self.partition(nums, start, end)
        while index != k:
            if index > k:
                index = self.partition(nums, start, index - 1)
            elif index < k:
                index = self.partition(nums, index + 1, end)
        return nums[:k]

# 这个是查找列表里第k大的值。


# 下面这个是针对快排特别好的一种写法。
def partition(array, l, r):
    x = array[r]
    print(x, r)
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            print(array, i, j)
            i += 1
            array[i], array[j] = array[j], array[i]
            print(array, i, j)
    array[i + 1], array[r] = array[r], array[i + 1]
    return array

array = [2, 4, 9, 8, 7, 3, 2, 6]
print(partition(array, 0, len(array) - 1))