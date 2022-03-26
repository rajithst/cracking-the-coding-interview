class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        char_frequency = {}
        for char in t:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        matched = 0
        for we in range(len(s)):
            char = s[we]
            if char in char_frequency:
                char_frequency[char] -= 1

                if char_frequency[char] == 0:
                    matched += 1
                if matched == len(char_frequency):
                    return True

        return False
