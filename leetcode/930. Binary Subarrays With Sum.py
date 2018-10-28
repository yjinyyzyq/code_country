# 930. Binary Subarrays With Sum

"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""

from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        d = defaultdict(int)
        ps, ans = 0, 0
        for a in A:
            d[ps] += 1
            ps += a
            ans += d[ps - S]
            print(ans, d)

        return ans


# Input = [1, 0, 1, 0, 1]
# S = 2
# print(Solution().numSubarraysWithSum(Input, S))

Input = [1,0, 0, 0, 0, 1, 1]
S = 0
print(Solution().numSubarraysWithSum(Input, S))
