# coding:utf-8
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a = "".join(
        #     [i for i in s if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 91 or 97 <= ord(i) <= 122]).lower()  # 这个是我自己的解题方法
        # return a == a[::-1]
        # ----------------------------------------------------------------------------------
        a = "".join([ch for ch in s if ch.isalnum()]).lower()  # 这种方式使用了isalnum方式，也比较好
        # isalnum, isalpha, isdigit, islower, isnumeric, isspace, istitle, isupper的用法。
        # isalnum就是判断字符串是否只包含数字和字母。
        # isalpha就是判断字符串是否只包含数字。
        # islower就是判断字符串是否字母都是小写。
        # isupper就是判断字符串是否字母都是大写。
        # isdigit就是判断字符串是否都是由数字组成。
        # isnumeric就是判断字符串是否只是由unicode数字组成。
        # isspace就是判断字符串是否只由空格组成。
        # istitle就是判断每个单词的开头是不是以大写开头。
        return a == a[::-1]


# 这种是最快的解题方法，但是不推荐。
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s_2 = s.replace(" ", "").replace(",", "").replace(".", "").replace(":", "").replace("@", "").replace("!", "") \
#             .replace("#", "").replace("$", "").replace("%", "").replace("&", "").replace("-", "").replace("?", ""). \
#             replace("\"", "").replace("\'", "").replace(";", "").replace("(", "").replace(")", "").replace("`", "")
#         s_2 = s_2.lower()
#         return s_2 == s_2[::-1]


a = Solution()
Input = "A man, a plan, a canal: Panama"
assert a.isPalindrome(Input) is True

Input = "race a car"
assert a.isPalindrome(Input) is False

Input = "`l;`` 1o1 ??;l`"
assert a.isPalindrome(Input) is True
