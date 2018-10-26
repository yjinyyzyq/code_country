# coding:utf-8
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = "aeiouAEIOU"  # 注意这里元音包含大小写。
        a = 0
        b = len(s) - 1
        c = list(s)
        while a < b:
            while s[a] not in vowel and a < b:
                a += 1
            while s[b] not in vowel and a < b:
                b -= 1
            if a >= b:
                break
            c[a], c[b] = c[b], c[a]
            a += 1
            b -= 1
        return "".join(c)


Input = "hello"
Output = "holle"
assert Solution().reverseVowels(Input) == Output

Input = "leetcode"
Output = "leotcede"
assert Solution().reverseVowels(Input) == Output

