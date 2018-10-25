# coding:utf-8
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = " ".join(reversed([i for i in s.split(" ") if i]))
        return a

print(Solution().reverseWords(" "))
print(" ".join("  ".split(" ")))

# 这个题就是反转一个单词，单词之间使用" "空格隔开的
# https://leetcode.com/problems/reverse-words-in-a-string/   151题