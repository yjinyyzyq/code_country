# coding:utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a, st = 0, 0
        dic = {}
        for key, i in enumerate(s):
            if i in dic and st <= len(s) - 2:
                if dic[i] >= st:
                    st = dic[i] + 1
            dic[i] = key
            a = max(key - st + 1, a)
        return a

assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("b") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("abba") == 2
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5
assert Solution().lengthOfLongestSubstring("dvdf") == 3

# 这个是求一个连续不重复的最大的字符串的长度


# 下面这个是另外一种解法。
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        ht = {}
        first = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in ht and first <= ht[s[i]]:
                first = ht[s[i]] + 1
            elif i - first + 1 > longest:
                longest = i - first + 1
            ht[s[i]] = i

        return longest