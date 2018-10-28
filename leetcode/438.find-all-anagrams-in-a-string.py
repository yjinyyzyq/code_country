from collections import defaultdict


# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         letter_required_num = defaultdict(int)
#         for letter in p:
#             letter_required_num[letter] += 1
#         num_missing = size_p = len(p)
#         res = []
#         for idx, letter in enumerate(s):
#             if letter_required_num[letter] > 0:
#                 num_missing -= 1
#             letter_required_num[letter] -= 1
#
#             if idx >= size_p:
#                 if letter_required_num[s[idx - size_p]] >= 0:
#                     num_missing += 1
#                 letter_required_num[s[idx - size_p]] += 1
#
#             if num_missing == 0:
#                 res.append(idx - size_p + 1)
#         return res


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        origin_dict, ret = {}, []
        for i in p:
            if i in origin_dict:
                origin_dict[i] += 1
            else:
                origin_dict[i] = 1
        missnum = l_p = len(p)
        for key, i in enumerate(s):
            if i in origin_dict:
                if origin_dict[i] > 0:
                    missnum -= 1
                origin_dict[i] -= 1

            if key >= l_p and s[key - l_p] in origin_dict:
                if origin_dict[s[key - l_p]] >= 0:
                    missnum += 1
                origin_dict[s[key - l_p]] += 1

            if missnum == 0:
                ret.append(key - l_p + 1)
        return ret


s = "cbaebabacd"
p = "abc"
Output = [0, 6]
print(Solution().findAnagrams(s, p))
assert Solution().findAnagrams(s, p) == Output

s = "abab"
p = "ab"
Output = [0, 1, 2]
assert Solution().findAnagrams(s, p) == Output

# https://blog.csdn.net/qq_17550379/article/details/80550907
