from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter1 = defaultdict(int)
        for letter in s:
            if counter1[letter]:
                counter1[letter] += 1
            else:
                counter1[letter] = 0

        counter2 = defaultdict(int)
        for letter in t:
            if counter2[letter]:
                counter2[letter] += 1
            else:
                counter2[letter] = 0

        if counter1 == counter2:
            return True
        else:
            return False


anagram = Solution()

print anagram.isAnagram('sas','sas')